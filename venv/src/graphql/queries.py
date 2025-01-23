import graphene
from src.graphql.types import Movie as MovieType, Genre as GenreType
from src.database.models import Movie as MovieModel, Genre as GenreModel
from sqlalchemy.orm import Session
from graphene import ObjectType, List, Field, Int, String

class Query(ObjectType):
    node = graphene.relay.Node.Field()
    all_movies = graphene.List(MovieType)
    all_genres = graphene.List(GenreType)
    movie = graphene.Field(MovieType, id=graphene.Int(required=True))
    genre = graphene.Field(GenreType, id=graphene.Int(required=True))
    movies_by_genre = List(MovieType, genre_id=Int(required=True))
    genre_by_movie = List(GenreType, movie_id=Int(required=True))


    def resolve_all_movies(root, info):
        db:Session = info.context.get("session")
        return db.query(MovieModel).all()

    def resolve_all_genres(root, info):
        db:Session = info.context.get("session")
        return db.query(GenreModel).all()

    def resolve_movie(root, info, id):
        db:Session = info.context.get("session")
        return db.query(MovieModel).get(id)

    def resolve_genre(root, info, id):
        db:Session = info.context.get("session")
        return db.query(GenreModel).get(id)

    def resolve_movies_by_genre(root, info, genre_id):
        db:Session = info.context.get("session")
        genre = db.query(GenreModel).get(genre_id)
        if genre:
            return genre.movies
        return []

    def resolve_genre_by_movie(root, info, movie_id):
        db:Session = info.context.get("session")
        movie = db.query(MovieModel).get(movie_id)
        if movie:
            return movie.genres
        return []