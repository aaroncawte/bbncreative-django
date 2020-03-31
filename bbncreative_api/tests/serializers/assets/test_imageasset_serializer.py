from django.core.files import File
from django.test import TestCase
from bbncreative_cms.models import Project, ImageAsset
from bbncreative_api.serializers import ImageAssetSerializer
from unittest import mock


class ImageAssetSerializerTests(TestCase):
    def test_imageasset_serializer_representation(self):
        parent_project = Project.objects.create()
        image_asset = ImageAsset.objects.create(parent=parent_project)

        representation = ImageAssetSerializer().to_representation(image_asset)

        self.assertEquals(representation["parent"], parent_project.id)

        # Core asset attributes
        self.assertEquals(representation["title"], "Asset Title")
        self.assertEquals(representation["body"], "Asset Body Text")
        self.assertEquals(representation["importance"], 0)

        # ImageAsset attributes
        self.assertEquals(representation["content"]["src"], None)
        self.assertEquals(representation["content"]["alt"], "")
        self.assertEquals(representation["content"]["ratio"], "W1")

        image_asset.delete()
        parent_project.delete()

    def test_customised_imageasset_serializer_representation(self):
        parent_project = Project.objects.create()
        image_asset = ImageAsset.objects.create(
            parent=parent_project,
            title="Arbitrary title",
            body="Some text for an ImageAsset",
            importance=12,
        )

        representation = ImageAssetSerializer().to_representation(image_asset)

        self.assertEquals(representation["parent"], parent_project.id)

        # Core asset attributes
        self.assertEquals(representation["title"], "Arbitrary title")
        self.assertEquals(representation["body"], "Some text for an ImageAsset")
        self.assertEquals(representation["importance"], 12)

        image_asset.delete()
        parent_project.delete()

    def test_mocked_imageasset_serializer_representation(self):

        image_mock = mock.MagicMock(spec=File, name="FileMock")
        image_mock.name = "mocked_img.jpg"

        parent_project = Project.objects.create()
        image_asset = ImageAsset.objects.create(
            parent=parent_project,
            img=image_mock,
            alt="Some alt text",
            aspect_ratio="T2",
        )

        representation = ImageAssetSerializer().to_representation(image_asset)

        self.assertEquals(representation["parent"], parent_project.id)

        # Core asset attributes
        self.assertEquals(representation["title"], "Asset Title")
        self.assertEquals(representation["body"], "Asset Body Text")
        self.assertEquals(representation["importance"], 0)

        # ImageAsset attributes
        self.assertEquals(representation["content"]["src"][-14:], "mocked_img.jpg")
        self.assertEquals(representation["content"]["alt"], "Some alt text")
        self.assertEquals(representation["content"]["ratio"], "T2")

        image_asset.delete()
        parent_project.delete()
