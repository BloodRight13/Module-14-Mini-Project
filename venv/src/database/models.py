from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

# Association Table for Movie-Genre Relationship (Many-to-Many)
movie_genre_association = Table(
    'movie_genre', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id'), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genres.id'), primary_key=True)
)


class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    release_year = Column(Integer)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    genres = relationship("Genre", secondary=movie_genre_association, back_populates="movies")

    def __repr__(self):
        return f"<Movie(title='{self.title}')>"


class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    movies = relationship("Movie", secondary=movie_genre_association, back_populates="genres")

    def __repr__(self):
        return f"<Genre(name='{self.name}')>"