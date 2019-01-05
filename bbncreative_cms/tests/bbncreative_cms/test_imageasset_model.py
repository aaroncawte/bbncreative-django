from django.test import TestCase

from bbncreative_cms import models


class ImageAssetTests(TestCase):

    def test_has_media(self):
        proj = models.Project.objects.create(name="Irrelevant Project")
        im = models.ImageAsset.objects.create(parent=proj, title="Test ImageAsset", body="Test Bio", alt="Test Alt")
        self.assertIs(im.has_media(), False)

    def test_image_with_no_project(self):
        image = models.ImageAsset.objects.create(title="Test ImageAsset", body="Test Bio", alt="Test Alt")
        id = image.id
        self.assertTrue(models.ImageAsset.objects.filter(id=image.id).exists())
        print(id)
        image.delete()
        self.assertFalse(models.ImageAsset.objects.filter(id=image.id).exists())

