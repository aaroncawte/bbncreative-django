from django.test import TestCase

from bbncreative_cms import models


class CollaboratorModelTests(TestCase):
    def test_get_collaborators(self):
        c1 = models.Collaborator.objects.create(name="Test Collaborator")
        c2 = models.Collaborator.objects.create(name="Test Collaborator")

        self.assertIs(models.Collaborator.objects.count(), 2)

        c1.delete()
        c2.delete()

    def test_default_values(self):
        c1 = models.Collaborator.objects.create()

        retrieved = models.Collaborator.objects.get(id=c1.id)

        self.assertEqual(retrieved.name, "Collaborator Name")
        self.assertEqual(retrieved.url, "")
        self.assertEqual(retrieved.twitter, "")

        c1.delete()

    def test_configured_values(self):
        c1 = models.Collaborator.objects.create(
            name="Test Name", url="https://bbncreative.co", twitter="bbncreative"
        )

        retrieved = models.Collaborator.objects.get(id=c1.id)

        self.assertEqual(retrieved.name, "Test Name")
        self.assertEqual(retrieved.url, "https://bbncreative.co")
        self.assertEqual(retrieved.twitter, "bbncreative")

        c1.delete()
