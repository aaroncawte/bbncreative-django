from rest_framework.test import APITestCase, APIClient
from bbncreative_cms.models import Project, Collaborator, Credit


def get_credits_endpoint(project_id):
    return "/api/project/" + str(project_id) + "/credits/"


class CreditEndpointTests(APITestCase):

    client = APIClient()

    def test_credits_endpoint_for_project_with_no_credits(self):
        project = Project.objects.create(name="Project with no collaborators")

        response = self.client.get(get_credits_endpoint(project.id), secure=True)
        data = response.data

        self.assertEquals(len(data), 0)

        project.delete()

    def test_credits_endpoint_for_project_with_one_credit(self):
        project = Project.objects.create(name="Example project")
        collaborator = Collaborator.objects.create()
        credit = Credit.objects.create(collaborator=collaborator, project=project)

        response = self.client.get(get_credits_endpoint(project.id), secure=True)
        data = response.data

        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]["collaborator"]["name"], "Collaborator Name")
        self.assertEquals(data[0]["collaborator"]["url"], "")

    def test_credits_endpoint_for_project_with_one_customised_credit(self):
        project = Project.objects.create()
        collaborator = Collaborator.objects.create(name="Great collaborator")
        credit = Credit.objects.create(
            collaborator=collaborator, project=project, action="Head of Passing Tests"
        )

        response = self.client.get(get_credits_endpoint(project.id), secure=True)
        data = response.data

        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]["collaborator"]["name"], "Great collaborator")
        self.assertEquals(data[0]["action"], "Head of Passing Tests")

    def test_credits_endpoint_for_project_with_multiple_credits(self):
        project = Project.objects.create(name="Example project")

        collaborator1 = Collaborator.objects.create(name="Human 1")
        collaborator2 = Collaborator.objects.create(name="Human 2")
        collaborator3 = Collaborator.objects.create(name="Human 3")

        credit1 = Credit.objects.create(
            collaborator=collaborator1, project=project, action="Doing Human 1 things"
        )
        credit2 = Credit.objects.create(
            collaborator=collaborator2, project=project, action="Doing Human 2 things"
        )
        credit3 = Credit.objects.create(
            collaborator=collaborator3, project=project, action="Doing Human 3 things"
        )

        response = self.client.get(get_credits_endpoint(project.id), secure=True)
        data = response.data

        self.assertEquals(len(data), 3)
        self.assertEquals(data[0]["collaborator"]["name"], "Human 3")
        self.assertEquals(data[1]["collaborator"]["name"], "Human 2")
        self.assertEquals(data[2]["collaborator"]["name"], "Human 1")

    def test_credits_endpoint_for_project_with_duplicated_credits(self):
        project = Project.objects.create(name="Example project")

        collaborator1 = Collaborator.objects.create(name="Human 1")
        collaborator2 = Collaborator.objects.create(name="Human 2")

        credit1 = Credit.objects.create(
            collaborator=collaborator1, project=project, action="Doing Human 1 things"
        )
        credit2 = Credit.objects.create(
            collaborator=collaborator2, project=project, action="Doing Human 2 things"
        )
        credit3 = Credit.objects.create(
            collaborator=collaborator2,
            project=project,
            action="Doing different Human 2 things",
        )

        response = self.client.get(get_credits_endpoint(project.id), secure=True)
        data = response.data

        self.assertEquals(len(data), 3)
        self.assertEquals(data[0]["collaborator"]["name"], collaborator2.name)
        self.assertEquals(data[1]["collaborator"]["name"], collaborator2.name)
        self.assertEquals(data[2]["collaborator"]["name"], collaborator1.name)

        self.assertEquals(data[0]["action"], credit3.action)
        self.assertEquals(data[1]["action"], credit2.action)
        self.assertEquals(data[2]["action"], credit1.action)
