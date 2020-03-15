import datetime
from django.core.files import File
from django.test import TestCase
from bbncreative_cms.models import Project
from bbncreative_api.serializers import ProjectSerializer
from unittest import mock


class ProjectSerializerTests(TestCase):

    def test_project_serializer_representation(self):
        project = Project.objects.create(name="Test Project")

        representation = ProjectSerializer().to_representation(project)

        self.assertEquals(representation['name'], 'Test Project')
        self.assertEquals(representation['shortName'], 'New Project')
        self.assertEquals(representation['description'], '[Project Bio]')
        self.assertEquals(representation['slug'], 'new-project')
        self.assertEquals(representation['progress']['complete'], False)
        self.assertEquals(representation['progress']['date'],
                          datetime.date.today().isoformat())
        self.assertEquals(representation['clientName'], 'New Client')
        self.assertEquals(representation['images']['icon'], None)
        self.assertEquals(representation['images']['hero'], None)
        self.assertEquals(representation['colors']['primary'], '455a64')
        self.assertEquals(representation['colors']['secondary'], '')
        self.assertEquals(
            representation['callToAction']['label'], 'Go to Website')
        self.assertEquals(
            representation['callToAction']['url'], 'https://bbncreative.co')

        project.delete()

    def test_customised_project_serializer_representation(self):
        project = Project.objects.create(
            name="Test Project 2",
            is_complete=True,
            date_complete='2020-04-01'
        )

        representation = ProjectSerializer().to_representation(project)

        self.assertEquals(representation['name'], 'Test Project 2')
        self.assertEquals(representation['shortName'], 'New Project')
        self.assertEquals(representation['description'], '[Project Bio]')
        self.assertEquals(representation['slug'], 'new-project')
        self.assertEquals(representation['progress']['complete'], True)
        self.assertEquals(representation['progress']['date'], '2020-04-01')
        self.assertEquals(representation['clientName'], 'New Client')
        self.assertEquals(representation['images']['icon'], None)
        self.assertEquals(representation['images']['hero'], None)
        self.assertEquals(representation['colors']['primary'], '455a64')
        self.assertEquals(representation['colors']['secondary'], '')
        self.assertEquals(
            representation['callToAction']['label'], 'Go to Website')
        self.assertEquals(
            representation['callToAction']['url'], 'https://bbncreative.co')

        project.delete()

    def test_project_with_images_serializer_representation(self):

        image_mock = mock.MagicMock(spec=File, name='FileMock')
        image_mock.name = 'mocked_img.jpg'

        project = Project.objects.create(
            icon=image_mock,
            hero=image_mock
        )

        representation = ProjectSerializer().to_representation(project)

        self.assertEquals(
            representation['images']['icon'][-14:], 'mocked_img.jpg')
        self.assertIsNotNone(
            representation['images']['hero'][-14:], 'mocked_img.jpg')

        project.delete()
