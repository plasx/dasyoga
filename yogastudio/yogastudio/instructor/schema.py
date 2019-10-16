import graphene
from graphene_django import DjangoObjectType

from .models import Instructor


class InstructorType(DjangoObjectType):
    class Meta:
        model = Instructor


class Query(graphene.ObjectType):
    instructors = graphene.List(InstructorType)

    def resolve_instructors(self, info, **kwargs):
        return Instructor.objects.all()
