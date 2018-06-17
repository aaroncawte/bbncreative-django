from django.test import TestCase
from bbncreative_cms import models


class DatabaseTestCases(TestCase):

    def test_get_collaborator_details_from_project(self):
        # Define a singular project, collaborator and credit, and query all details.
        print("Hello")

    # Two projects that share a collaborator and each have an independent second
    def test_shared_and_independent_collaborators(self):
        proj1 = models.Project(name="Test Project")
        proj2 = models.Project(name="Test Project")

        collab_shared = models.Collaborator(
            name="Alice",
            url="https://bbncreative.co/alice",
            twitter="bbn_alice"
        )
        collab_split1 = models.Collaborator(
            name="Bob",
            url="https://bbncreative.co/bob",
            twitter="bbn_bob"
        )
        collab_split2 = models.Collaborator(
            name="Charlie",
            url="https://bbncreative.co/charlie",
            twitter="bbn_charlie"
        )

        credit_pr1_shared = models.Credit(
            collaborator=collab_shared,
            project=proj1,
            action="Lorem Ipsum"
        )
        credit_pr1_split = models.Credit(
            collaborator=collab_split1,
            project=proj1,
            action="Lorem Ipsum"
        )
        credit_pr2_shared = models.Credit(
            collaborator=collab_shared,
            project=proj2,
            action="Lorem Ipsum"
        )
        credit_pr2_split = models.Credit(
            collaborator=collab_split2,
            project=proj2,
            action="Lorem Ipsum"
        )

        # Assert collab_shared has 2 projects
        # Assert each collab_split has 1 project
        # Assert each project has 2 collaborators, and who they are

    def test_create_project_with_three_collaborators(self):
        proj = models.Project(name="Test Project")
        collab1 = models.Collaborator(
            name="Alice",
            url="https://bbncreative.co/alice",
            twitter="bbn_alice"
        )
        collab2 = models.Collaborator(
            name="Bob",
            url="https://bbncreative.co/bob",
            twitter="bbn_bob"
        )
        collab3 = models.Collaborator(
            name="Charlie",
            url="https://bbncreative.co/charlie",
            twitter="bbn_charlie"
        )

        credit1 = models.Credit(
            collaborator=collab1,
            project=proj,
            action="Lead Developer"
        )
        credit2 = models.Credit(
            collaborator=collab2,
            project=proj,
            action="Product Design"
        )
        credit3 = models.Credit(
            collaborator=collab3,
            project=proj,
            action="Product Tester"
        )

        # Ensure that 3 credits are associated with this project

