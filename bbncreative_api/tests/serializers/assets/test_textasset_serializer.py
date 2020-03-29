from django.test import TestCase
from bbncreative_cms.models import Project, TextAsset
from bbncreative_api.serializers import TextAssetSerializer


class TextAssetSerializerTests(TestCase):

    def test_textasset_serializer_representation(self):
        parent_project = Project.objects.create()

        text_asset = TextAsset.objects.create(parent=parent_project)

        representation = TextAssetSerializer().to_representation(text_asset)

        self.assertEquals(representation['parent'], parent_project.id)

        # Core asset attributes
        self.assertEquals(representation['title'], 'Asset Title')
        self.assertEquals(representation['body'], 'Asset Body Text')
        self.assertEquals(representation['importance'], 0)

        text_asset.delete()
        parent_project.delete()

    def test_customised_textasset_serializer_representation(self):
        parent_project = Project.objects.create()

        text_asset = TextAsset.objects.create(
            parent=parent_project,
            title='Arbitrary title',
            body='Some text for a TextAsset',
            importance=12
        )

        representation = TextAssetSerializer().to_representation(text_asset)

        self.assertEquals(representation['parent'], parent_project.id)

        # Core asset attributes
        self.assertEquals(representation['title'], 'Arbitrary title')
        self.assertEquals(representation['body'], 'Some text for a TextAsset')
        self.assertEquals(representation['importance'], 12)

        text_asset.delete()
        parent_project.delete()
