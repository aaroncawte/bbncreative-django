from django.test import TestCase

from bbncreative_cms import models


class CollaboratorCreditNuanceTests(TestCase):

    # Two projects that share a collaborator and each have an independent second
    def test_shared_and_independent_collaborators(self):
        proj1 = models.Project.objects.create(name="Test Project", url_name="proj-1")
        proj2 = models.Project.objects.create(name="Test Project", url_name="proj-2")

        collab_shared = models.Collaborator.objects.create(
            name="Alice", url="https://bbncreative.co/alice", twitter="bbn_alice"
        )
        collab_split1 = models.Collaborator.objects.create(
            name="Bob", url="https://bbncreative.co/bob", twitter="bbn_bob"
        )
        collab_split2 = models.Collaborator.objects.create(
            name="Charlie", url="https://bbncreative.co/charlie", twitter="bbn_charlie"
        )

        credit_pr1_shared = models.Credit.objects.create(
            collaborator=collab_shared, project=proj1, action="Lorem Ipsum"
        )
        credit_pr1_split = models.Credit.objects.create(
            collaborator=collab_split1, project=proj1, action="Lorem Ipsum"
        )
        credit_pr2_shared = models.Credit.objects.create(
            collaborator=collab_shared, project=proj2, action="Lorem Ipsum"
        )
        credit_pr2_split = models.Credit.objects.create(
            collaborator=collab_split2, project=proj2, action="Lorem Ipsum"
        )

        # Assert collab_shared has 2 projects
        self.assertEqual(
            models.Credit.objects.filter(collaborator=collab_shared).count(), 2
        )

        # Assert each collab_split has 1 project
        self.assertEqual(
            models.Credit.objects.filter(collaborator=collab_split1).count(), 1
        )
        self.assertEqual(
            models.Credit.objects.filter(collaborator=collab_split2).count(), 1
        )

        # Assert each project has 2 collaborators
        self.assertEqual(models.Credit.objects.filter(project=proj1).count(), 2)
        self.assertEqual(models.Credit.objects.filter(project=proj2).count(), 2)

    # Ensure that 3 credits are associated with this project
    def test_3_credits_3_collaborators(self):
        proj = models.Project.objects.create(name="Test Project")
        collab1 = models.Collaborator.objects.create(
            name="Alice", url="https://bbncreative.co/alice", twitter="bbn_alice"
        )
        collab2 = models.Collaborator.objects.create(
            name="Bob", url="https://bbncreative.co/bob", twitter="bbn_bob"
        )
        collab3 = models.Collaborator.objects.create(
            name="Charlie", url="https://bbncreative.co/charlie", twitter="bbn_charlie"
        )

        credit1 = models.Credit.objects.create(
            collaborator=collab1, project=proj, action="Lead Developer"
        )
        credit2 = models.Credit.objects.create(
            collaborator=collab2, project=proj, action="Product Design"
        )
        credit3 = models.Credit.objects.create(
            collaborator=collab3, project=proj, action="Product Tester"
        )

        self.assertIs(
            models.Credit.objects.filter(project=proj).count(), 3
        )  # 3 credits are associated with this project
        self.assertIs(
            proj.count_collaborators(), 3
        )  # 3 collaborators are found from all credits

    def test_2_credits_1_collaborator(self):
        proj = models.Project.objects.create(name="Test Project")

        collab1 = models.Collaborator.objects.create(
            name="Alice", url="https://bbncreative.co/alice", twitter="bbn_alice"
        )

        credit1 = models.Credit.objects.create(
            collaborator=collab1, project=proj, action="Lead Developer"
        )

        credit2 = models.Credit.objects.create(
            collaborator=collab1, project=proj, action="Product Design"
        )

        # One collaborator is credited with 2 things - are the counts right?
        self.assertIs(models.Credit.objects.filter(project=proj).count(), 2)
        self.assertIs(proj.count_collaborators(), 1)
