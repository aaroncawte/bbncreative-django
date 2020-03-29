from rest_framework.test import APITestCase, APIClient
from bbncreative_cms.models import Project, TextAsset


def get_textasset_by_project_endpoint(project_id):
    return '/api/project/' + str(project_id) + '/assets/text/'


class TextAssetByProjectEndpointTests(APITestCase):

    client = APIClient()

    def test_textasset_by_project_endpoint_for_project_with_no_textassets(self):
        project = Project.objects.create()

        response = self.client.get(
            get_textasset_by_project_endpoint(project.id),
            secure=True
        )
        data = response.data

        self.assertEquals(len(data), 0)

        project.delete()

    def test_textasset_by_project_endpoint_for_project_with_two_textassets(self):
        project = Project.objects.create()
        asset1 = TextAsset.objects.create(
            parent=project, title='Asset 1')
        asset2 = TextAsset.objects.create(
            parent=project, title='Asset 2')

        response = self.client.get(
            get_textasset_by_project_endpoint(project.id),
            secure=True
        )
        data = response.data

        self.assertEquals(len(data), 2)
        self.assertEquals(data[0]['title'], 'Asset 2')
        self.assertEquals(data[1]['title'], 'Asset 1')

        project.delete()

    def test_textasset_by_project_endpoint_for_importance_sorting(self):
        project = Project.objects.create()
        asset1 = TextAsset.objects.create(
            parent=project, title='More important asset', importance=0)
        asset2 = TextAsset.objects.create(
            parent=project, title='Less important asset', importance=1)

        response = self.client.get(
            get_textasset_by_project_endpoint(project.id),
            secure=True
        )
        data = response.data

        self.assertEquals(len(data), 2)
        self.assertEquals(data[0]['title'], 'More important asset')
        self.assertEquals(data[1]['title'], 'Less important asset')

        project.delete()
