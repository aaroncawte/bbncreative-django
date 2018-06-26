from django.test import TestCase
from bbncreative_cms import models


class DatabaseTestCases(TestCase):

    # Define a singular project, collaborator and credit, and query all details.
    def test_get_collaborator_details_from_project(self):
        proj = models.Project(name="Test Project")
        collab = models.Collaborator(
            name="Alice",
            url="https://bbncreative.co",
            twitter="bbn_alice"
        )
        credit = models.Credit(
            collaborator=collab,
            project=proj,
            action="Test Action Line"
        )
        self.assertIs(proj.name, "Test Project")
        self.assertIs(collab.name, "Alice")
        self.assertIs(collab.url, "https://bbncreative.co")
        self.assertIs(collab.twitter, "bbn_alice")
        self.assertIs(credit.action, "Test Action Line"),
        self.assertIs(credit.project.name, "Test Project"),
        self.assertIs(credit.collaborator.twitter, "bbn_alice")

    # Two projects that share a collaborator and each have an independent second
    def test_shared_and_independent_collaborators(self):
        proj1 = models.Project.objects.create(name="Test Project")
        proj2 = models.Project.objects.create(name="Test Project")

        collab_shared = models.Collaborator.objects.create(
            name="Alice",
            url="https://bbncreative.co/alice",
            twitter="bbn_alice"
        )
        collab_split1 = models.Collaborator.objects.create(
            name="Bob",
            url="https://bbncreative.co/bob",
            twitter="bbn_bob"
        )
        collab_split2 = models.Collaborator.objects.create(
            name="Charlie",
            url="https://bbncreative.co/charlie",
            twitter="bbn_charlie"
        )

        credit_pr1_shared = models.Credit.objects.create(
            collaborator=collab_shared,
            project=proj1,
            action="Lorem Ipsum"
        )
        credit_pr1_split = models.Credit.objects.create(
            collaborator=collab_split1,
            project=proj1,
            action="Lorem Ipsum"
        )
        credit_pr2_shared = models.Credit.objects.create(
            collaborator=collab_shared,
            project=proj2,
            action="Lorem Ipsum"
        )
        credit_pr2_split = models.Credit.objects.create(
            collaborator=collab_split2,
            project=proj2,
            action="Lorem Ipsum"
        )

        # Assert collab_shared has 2 projects
        self.assertEqual(models.Credit.objects.filter(collaborator=collab_shared).count(), 2)

        # Assert each collab_split has 1 project
        self.assertEqual(models.Credit.objects.filter(collaborator=collab_split1).count(), 1)
        self.assertEqual(models.Credit.objects.filter(collaborator=collab_split2).count(), 1)

        # Assert each project has 2 collaborators
        self.assertEqual(models.Credit.objects.filter(project=proj1).count(), 2)
        self.assertEqual(models.Credit.objects.filter(project=proj2).count(), 2)

    # Ensure that 3 credits are associated with this project
    def test_create_project_with_three_collaborators(self):
        proj = models.Project.objects.create(name="Test Project")
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
        collab3 = models.Collaborator.objects.create(
            name="Charlie",
            url="https://bbncreative.co/charlie",
            twitter="bbn_charlie"
        )

        credit1 = models.Credit.objects.create(
            collaborator=collab1,
            project=proj,
            action="Lead Developer"
        )
        credit2 = models.Credit.objects.create(
            collaborator=collab2,
            project=proj,
            action="Product Design"
        )
        credit3 = models.Credit.objects.create(
            collaborator=collab3,
            project=proj,
            action="Product Tester"
        )

        self.assertIs(models.Credit.objects.filter(project=proj).count(), 3)
