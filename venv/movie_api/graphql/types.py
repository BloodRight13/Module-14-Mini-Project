import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from src.database.models import Movie as MovieModel, Genre as GenreModel

class Movie(SQLAlchemyObjectType):
    class Meta:
        model = MovieModel

class Genre(SQLAlchemyObjectType):
    class Meta:
        model = GenreModel
