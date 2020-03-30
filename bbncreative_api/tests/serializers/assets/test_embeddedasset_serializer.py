from django.core.files import File
from django.test import TestCase
from bbncreative_cms.models import Project, EmbeddedAsset
from bbncreative_api.serializers import EmbeddedAssetSerializer
from unittest import mock


class EmbeddedAssetSerializerTests(TestCase):
    def test_embeddedasset_serializer_representation(self):
        parent_project = Project.objects.create()
        embedded_asset = EmbeddedAsset.objects.create(parent=parent_project)

        representation = EmbeddedAssetSerializer().to_representation(embedded_asset)

        self.assertEquals(representation["parent"], parent_project.id)

        # Core asset attributes
        self.assertEquals(representation["title"], "Asset Title")
        self.assertEquals(representation["body"], "Asset Body Text")
        self.assertEquals(representation["importance"], 0)

        # EmbeddedAsset attributes
        self.assertEquals(representation["content"]["code"], "")
        self.assertEquals(representation["content"]["ratio"], "VL")

        embedded_asset.delete()
        parent_project.delete()

    def test_customised_embeddedasset_serializer_representation(self):
        parent_project = Project.objects.create()
        embedded_asset = EmbeddedAsset.objects.create(
            parent=parent_project,
            title="Custom title",
            body="Text to go alongside",
            importance=12,
            embed_code="<iframe></iframe>",
            aspect_ratio="T1",
        )

        representation = EmbeddedAssetSerializer().to_representation(embedded_asset)

        self.assertEquals(representation["parent"], parent_project.id)

        # Core asset attributes
        self.assertEquals(representation["title"], "Custom title")
        self.assertEquals(representation["body"], "Text to go alongside")
        self.assertEquals(representation["importance"], 12)

        # EmbeddedAsset attributes
        self.assertEquals(representation["content"]["code"], "<iframe></iframe>")
        self.assertEquals(representation["content"]["ratio"], "T1")

        embedded_asset.delete()
        parent_project.delete()
