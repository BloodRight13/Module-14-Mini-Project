import graphene
from graphene import ObjectType, String, Int, ID, Field
from src.database.models import Genre as GenreModel, Movie as MovieModel
from src.graphql.types import Genre as GenreType, Movie as MovieType
from sqlalchemy.orm import Session
from src.utils.validators import validate_genre_name

class CreateGenre(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    Output = GenreType

    def mutate(root, info, name):
        validate_genre_name(name)  # Example validation
        db: Session = info.context.get("session")
        genre = GenreModel(name=name)
        db.add(genre)
        db.commit()
        db.refresh(genre)
        return genre

class UpdateGenre(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)

    Output = GenreType

    def mutate(root, info, id, name):
        validate_genre_name(name)
        db: Session = info.context.get("session")
        genre = db.query(GenreModel).get(id)
        if not genre:
            raise Exception("Genre not found")
        genre.name = name
        db.commit()
        db.refresh(genre)
        return genre


class DeleteGenre(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    Output = graphene.Boolean

    def mutate(root, info, id):
        db: Session = info.context.get("session")
        genre = db.query(GenreModel).get(id)
        if not genre:
            raise Exception("Genre not found")
        db.delete(genre)
        db.commit()
        return True


class CreateMovie(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()
        release_year = graphene.Int()
        genre_ids = graphene.List(graphene.Int)

    Output = MovieType

    def mutate(root, info, title, description=None, release_year=None, genre_ids=None):
        db: Session = info.context.get("session")
        movie = MovieModel(title=title, description=description, release_year=release_year)

        if genre_ids:
            genres = db.query(GenreModel).filter(GenreModel.id.in_(genre_ids)).all()
            movie.genres = genres

        db.add(movie)
        db.commit()
        db.refresh(movie)
        return movie


class UpdateMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        description = graphene.String()
        release_year = graphene.Int()
        genre_ids = graphene.List(graphene.Int)

    Output = MovieType

    def mutate(root, info, id, title=None, description=None, release_year=None, genre_ids=None):
        db: Session = info.context.get("session")
        movie = db.query(MovieModel).get(id)
        if not movie:
            raise Exception("Movie not found")

        if title:
            movie.title = title
        if description:
            movie.description = description
        if release_year:
            movie.release_year = release_year

        if genre_ids:
            genres = db.query(GenreModel).filter(GenreModel.id.in_(genre_ids)).all()
            movie.genres = genres

        db.commit()
        db.refresh(movie)
        return movie


class DeleteMovie(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    Output = graphene.Boolean

    def mutate(root, info, id):
        db: Session = info.context.get("session")
        movie = db.query(MovieModel).get(id)
        if not movie:
            raise Exception("Movie not found")
        db.delete(movie)
        db.commit()
        return True

class Mutation(ObjectType):
  create_genre = CreateGenre.Field()
  update_genre = UpdateGenre.Field()
  delete_genre = DeleteGenre.Field()
  create_movie = CreateMovie.Field()
  update_movie = UpdateMovie.Field()
  delete_movie = DeleteMovie.Field()