import graphene

import yogastudio.instructor.schema

class Query(yogastudio.instructor.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)