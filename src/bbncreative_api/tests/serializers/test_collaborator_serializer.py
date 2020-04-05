from django.test import TestCase
from bbncreative_cms.models import Collaborator
from bbncreative_api.serializers import CollaboratorSerializer


class CollaboratorSerializerTests(TestCase):
    def test_collaborator_serializer_representation(self):
        collaborator = Collaborator.objects.create()

        representation = CollaboratorSerializer().to_representation(collaborator)

        self.assertEquals(representation["name"], "Collaborator Name")
        self.assertEquals(representation["url"], "")
        self.assertEquals(representation["twitter"], "")

        collaborator.delete()

    def test_customised_collaborator_serializer_representation(self):
        collaborator = Collaborator.objects.create(
            name="Fake Name", url="https://bbncreative.co", twitter="bbncreative"
        )

        representation = CollaboratorSerializer().to_representation(collaborator)

        self.assertEquals(representation["name"], "Fake Name")
        self.assertEquals(representation["url"], "https://bbncreative.co")
        self.assertEquals(representation["twitter"], "bbncreative")

        collaborator.delete()
