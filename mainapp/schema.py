import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from mainapp.models import ChallengeTag, ChallengeAudience, Challenges, Preapproved_challenge
from django.contrib.auth.decorators import login_required

class ChallengeTagType(DjangoObjectType):
    class Meta:
        model = ChallengeTag

class ChallengeAudienceType(DjangoObjectType):
    class Meta:
        model = ChallengeAudience

class ChallengesType(DjangoObjectType):
    class Meta:
        model = Challenges

    def resolve_image(self, info):
            image = info.context.build_absolute_uri(self.image.url)
            return image

class Preapproved_challengeType(DjangoObjectType):
    class Meta:
        model = Preapproved_challenge

class Query(graphene.ObjectType):
    challengetag = graphene.List(ChallengeTagType)
    challengeaudience = graphene.List(ChallengeAudienceType)
    challenges = graphene.List(ChallengesType)
    challenge = graphene.Field(ChallengesType, id=graphene.Int())

    def resolve_challengetag(self, info, **kwargs):
        return ChallengeTag.objects.all()

    def resolve_challengeaudience(self, info, **kwargs):
        return ChallengeAudience.objects.all()

    def resolve_challenges(self, info, **kwargs):
        return Challenges.objects.all()

    def resolve_challenge(self, info, id):
        return Challenges.objects.get(pk=id)


schema = graphene.Schema(query=Query)




# class PreapprovedChallengeInput(graphene.InputObjectType):
#     id = graphene.ID()
#     goal - graphene.String()
#     name = graphene.String()
#     external_url = graphene.String()
#     length = graphene.String()
#     short_description = graphene.String()
#     steps_to_complete = graphene.String()
#     why = graphene.String()
#     tips = graphene.String()
#     tags = graphene.List(ChallengeTagInput)


# class CreatePreapprovedChallenge(graphene.Mutation):
#     class Arguments:
#         input = PreapprovedChallengeInput(required=True)

#     ok = graphene.Boolean()
#     goal = graphene.Field(Preapproved_challengeType)
#     name = graphene.Field(Preapproved_challengeType)
#     external_url = graphene.Field(Preapproved_challengeType)
#     length = graphene.Field(Preapproved_challengeType)
#     short_description = graphene.Field(Preapproved_challengeType)
#     steps_to_complete = graphene.Field(Preapproved_challengeType)
#     why = graphene.Field(Preapproved_challengeType)
#     tips = graphene.Field(Preapproved_challengeType)
#     tags = graphene.Field(Preapproved_challengeType)

#     @staticmethod
#     @login_required
#     def mutate(root, info, input=None):
#         ok = True
#         preapprovedchallenge_instance = Preapproved_challenge(
#             goal=input.goal,
#             name=input.name,
#             external_url=input.external_url,
#             length=input.length,
#             short_description=input.short_description,
#             steps_to_complete=input.steps_to_complete,
#             why=input.why,
#             tips=input.tips,
#             tags=input.tags
#             )
#         preapprovedchallenge_instance.save()
#         return CreatePreapprovedChallenge(ok=ok, )
