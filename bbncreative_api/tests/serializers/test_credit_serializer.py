from django.test import TestCase
from bbncreative_cms.models import Collaborator, Credit, Project
from bbncreative_api.serializers import CreditSerializer


class CreditSerializerTests(TestCase):

    def test_credit_serializer_representation(self):
        project = Project.objects.create(name='Test Project')
        collaborator = Collaborator.objects.create(
            name='Test Writer',
            twitter='bbncreative'
        )
        credit = Credit.objects.create(
            collaborator=collaborator, project=project)

        representation = CreditSerializer().to_representation(credit)

        self.assertEquals(representation['action'], '')
        self.assertEquals(
            representation['collaborator']['name'], 'Test Writer')
        self.assertEquals(
            representation['collaborator']['twitter'], 'bbncreative')

        credit.delete()
        collaborator.delete()
        project.delete()

    def test_customised_collaborator_serializer_representation(self):
        project = Project.objects.create(name='Test Project')
        collaborator = Collaborator.objects.create()
        credit = Credit.objects.create(
            collaborator=collaborator,
            project=project,
            action='Tester'
        )

        representation = CreditSerializer().to_representation(credit)

        self.assertEquals(representation['action'], 'Tester')

        credit.delete()
        collaborator.delete()
        project.delete()
