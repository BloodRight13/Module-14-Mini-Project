from flask import Flask, request
from flask_graphql import GraphQLView
from src.graphql.schema import schema
from src.database.database import create_db_and_tables, get_db
from sqlalchemy.orm import Session

app = Flask(__name__)
app.debug = True

create_db_and_tables() # Create tables if they don't exist

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,  # for having the GraphiQL interface
        get_context=lambda: {"session": get_db().__next__()}  # Access the database session
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db:Session = get_db().__next__()
    if db:
        db.close()

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()