import graphene
import beelinechallenges.mainapp.schema

class Query(beelinechallenges.mainapp.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)