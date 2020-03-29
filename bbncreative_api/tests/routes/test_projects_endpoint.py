from rest_framework.test import APITestCase, APIClient
from bbncreative_cms.models import Project

PROJECTS_ENDPOINT = '/api/projects/'


class ProjectEndpointTests(APITestCase):

    client = APIClient()

    def test_projects_endpoint_with_no_data(self):
        response = self.client.get(PROJECTS_ENDPOINT, secure=True)
        data = response.data

        self.assertEquals(len(data), 0)

    def test_projects_endpoint_with_one_blank_project(self):
        project = Project.objects.create(name='Test')

        response = self.client.get(PROJECTS_ENDPOINT, secure=True)
        data = response.data

        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]['name'], 'Test')
        self.assertEquals(data[0]['progress']['complete'], False)
        self.assertEquals(
            data[0]['callToAction']['label'], 'Go to Website')

        project.delete()

    def test_projects_endpoint_with_three_blank_projects(self):
        project1 = Project.objects.create(name='Test 1')
        project2 = Project.objects.create(name='Test 2')
        project3 = Project.objects.create(name='Test 3')

        response = self.client.get(PROJECTS_ENDPOINT, secure=True)
        data = response.data

        self.assertEquals(len(data), 3)
        self.assertEquals(data[0]['name'], 'Test 1')
        self.assertEquals(data[1]['name'], 'Test 2')
        self.assertEquals(data[2]['name'], 'Test 3')

        project1.delete()
        project2.delete()
        project3.delete()
