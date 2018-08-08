from django.test import TestCase

from bbncreative_cms import models


class EmbeddedAssetTests(TestCase):

    def test_has_media(self):
        proj = models.Project.objects.create(name="Irrelevant Project")
        em_no_media = models.EmbeddedAsset.objects.create(parent=proj, title="Test EmbeddedAsset", body="Test Bio")
        self.assertIs(em_no_media.has_media(), False)

        em_has_media = models.EmbeddedAsset.objects.create(
            parent=proj,
            title="Test EmbeddedAsset",
            body="Test Bio",
            embed_code="<html><p>Example Embed Code</html>"
        )
        self.assertIs(em_has_media.has_media(), True)
