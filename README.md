# Movie Genre GraphQL API

This project implements a GraphQL API for managing movies and genres, built with Python, Flask, SQLAlchemy, and Graphene.

## Features

*   **Data Modeling:**  Defines database models for movies and genres with relationships.
*   **GraphQL Interface:** Provides a GraphQL API for querying and manipulating movie and genre data.
*   **CRUD Operations:** Supports Create, Read, Update, and Delete (CRUD) operations for both movies and genres through GraphQL mutations.
*   **Relationships:** Handles relationships between movies and genres (a movie can have multiple genres, and a genre can be associated with multiple movies).
*   **Data Validation:** Includes input validation for genre names.
*   **Database Interaction:** Uses SQLAlchemy for database interaction and ORM functionality.
*   **Example Queries and Mutations:** Provides example GraphQL queries and mutations for common operations.

## Technologies Used

*   **Python 3.8+**
*   **Flask:**  Web framework for building the API.
*   **SQLAlchemy:**  ORM for interacting with the database.
*   **Graphene:**  Library for building GraphQL APIs in Python.
*   **Flask-GraphQL:** Integrates GraphQL with Flask.
*   **psycopg2-binary** (or your preferred database driver): Database adapter for PostgreSQL.

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd movie-genre-graphql-api
    ```

2.  **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure the database:**

    *   Ensure you have a PostgreSQL (or your chosen database) server running.
    *   Create a database for the application.
    *   Update the `DATABASE_URL` in `src/database/database.py` with your database credentials:

        ```python
        DATABASE_URL = "postgresql://user:password@host:port/database_name"
        ```

        Replace `user`, `password`, `host`, `port`, and `database_name` with your actual database credentials.

5.  **Run the application:**

    ```bash
    python src/app.py
    ```

    The API will be accessible at `http://127.0.0.1:5000/graphql` (or the address your Flask app is running on).

## Usage

Open your browser and navigate to `http://127.0.0.1:5000/graphql` to access the GraphiQL interface.  This allows you to explore the GraphQL schema and execute queries and mutations.

### Example Queries

*   **Get all genres:**

    ```graphql
    query {
      allGenres {
        id
        name
      }
    }
    ```

*   **Get movies by genre ID:**

    ```graphql
    query {
      moviesByGenre(genreId: 1) {
        id
        title
      }
    }
    ```

*   **Get a genre by movie ID:**

    ```graphql
    query {
      genreByMovie(movieId: 1) {
        id
        name
      }
    }
    ```

*   **Get all movies:**

   ```graphql
    query{
      allMovies{
        id
        title
        description
        releaseYear
        genres{
          id
          name
        }
      }
    }