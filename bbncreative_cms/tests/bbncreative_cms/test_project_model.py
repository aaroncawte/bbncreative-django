from django.test import TestCase

from bbncreative_cms import models


class ProjectModelTests(TestCase):

    def test_get_text_assets(self):
        proj = models.Project.objects.create(name="Test Project")

        asset1 = models.TextAsset.objects.create(
            parent=proj,
            title="Asset Title 1",
            body="Asset Body",
            importance=0
        )

        # Count text assets, verify ordering
        self.assertIs(len(proj.get_text_assets()), 1)
        self.assertEqual(proj.get_text_assets()[0].title, "Asset Title 1")

        asset2 = models.TextAsset.objects.create(
            parent=proj,
            title="Asset Title 2",
            body="Asset Body",
            importance=1
        )

        # Count text assets, verify ordering
        self.assertIs(len(proj.get_text_assets()), 2)
        self.assertEqual(proj.get_text_assets()[1].title, "Asset Title 2")

        # Ensure these assets are not incorrectly found by other functions
        self.assertIs(len(proj.get_image_assets()), 0)
        self.assertIs(len(proj.get_embedded_assets()), 0)

    def test_get_image_assets(self):
        proj = models.Project.objects.create(name="Test Project")

        asset1 = models.ImageAsset.objects.create(
            parent=proj,
            title="Asset Title 1",
            body="Asset Body",
            importance=0
        )

        # Count text assets, verify ordering
        self.assertIs(len(proj.get_image_assets()), 1)
        self.assertEqual(proj.get_image_assets()[0].title, "Asset Title 1")

        asset2 = models.ImageAsset.objects.create(
            parent=proj,
            title="Asset Title 2",
            body="Asset Body",
            importance=1
        )

        # Count text assets, verify ordering
        self.assertIs(len(proj.get_image_assets()), 2)
        self.assertEqual(proj.get_image_assets()[1].title, "Asset Title 2")

        # Ensure these assets are not incorrectly found by other functions
        self.assertIs(len(proj.get_text_assets()), 0)
        self.assertIs(len(proj.get_embedded_assets()), 0)

    def test_get_embedded_assets(self):
        proj = models.Project.objects.create(name="Test Project")

        asset1 = models.EmbeddedAsset.objects.create(
            parent=proj,
            title="Asset Title 1",
            body="Asset Body",
            importance=0,
            embed_code="<html><p>Hello, world.</p></html>"
        )

        # Count text assets, verify ordering
        self.assertIs(len(proj.get_embedded_assets()), 1)
        self.assertEqual(proj.get_embedded_assets()[0].title, "Asset Title 1")

        asset2 = models.EmbeddedAsset.objects.create(
            parent=proj,
            title="Asset Title 2",
            body="Asset Body",
            importance=1,
            embed_code="<html><p>Hello, world.</p></html>"
        )

        # Count text assets, verify ordering
        self.assertIs(len(proj.get_embedded_assets()), 2)
        self.assertEqual(proj.get_embedded_assets()[1].title, "Asset Title 2")

        # Ensure these assets are not incorrectly found by other functions
        self.assertIs(len(proj.get_text_assets()), 0)
        self.assertIs(len(proj.get_image_assets()), 0)

    def test_count_assets(self):
        proj = models.Project.objects.create(name="Test Project")

        im = models.ImageAsset.objects.create(parent=proj, title="Test ImageAsset", body="Test Bio", alt="Test Alt")
        self.assertIs(proj.count_assets(), 1)

        em = models.EmbeddedAsset.objects.create(parent=proj, title="Test EmbeddedAsset", body="Test Bio")
        self.assertIs(proj.count_assets(), 2)

        tx = models.TextAsset.objects.create(parent=proj, title="Test TextAsset", body="Test Bio")
        self.assertIs(proj.count_assets(), 3)

    def test_project_count_collaborators(self):
        project_with_no_collaborators = models.Project.objects.create(name="Project with 0 collaborators")
        project_with_one_collaborator = models.Project.objects.create(name="Project with 1 collaborator")
        project_with_two_collaborators = models.Project.objects.create(name="Project with 2 collaborators")

        collab1 = models.Collaborator.objects.create(
            name="Alice",
            url="https://bbncreative.co/alice",
            twitter="bbn_alice"
        )
        collab2 = models.Collaborator.objects.create(
            name="Bob",
            url="https://bbncreative.co/bob",
            twitter="bbn_bob"
        )

        credit_for_first_project = models.Credit.objects.create(
            project=project_with_one_collaborator,
            collaborator=collab1
        )
        credit_1_for_second_project = models.Credit.objects.create(
            project=project_with_two_collaborators,
            collaborator=collab1
        )
        credit_2_for_second_project = models.Credit.objects.create(
            project=project_with_two_collaborators,
            collaborator=collab2
        )

        self.assertIs(project_with_no_collaborators.count_collaborators(), 0)
        self.assertIs(project_with_one_collaborator.count_collaborators(), 1)
        self.assertIs(project_with_two_collaborators.count_collaborators(), 2)
