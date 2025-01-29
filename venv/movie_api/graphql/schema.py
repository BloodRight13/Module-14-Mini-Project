import graphene
from src.graphql.queries import Query
from src.graphql.mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
