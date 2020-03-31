from rest_framework.test import APITestCase, APIClient
from bbncreative_cms.models import Project, EmbeddedAsset


def get_embeddedasset_by_project_endpoint(project_id):
    return "/api/project/" + str(project_id) + "/assets/embedded/"


class EmbeddedAssetByProjectEndpointTests(APITestCase):

    client = APIClient()

    def test_embeddedasset_by_project_endpoint_for_project_with_no_embeddedassets(self):
        project = Project.objects.create()

        response = self.client.get(
            get_embeddedasset_by_project_endpoint(project.id), secure=True
        )
        data = response.data

        self.assertEquals(len(data), 0)

        project.delete()

    def test_embeddedasset_by_project_endpoint_for_project_with_two_embeddedassets(
        self,
    ):
        project = Project.objects.create()
        asset1 = EmbeddedAsset.objects.create(parent=project, title="Asset 1")
        asset2 = EmbeddedAsset.objects.create(parent=project, title="Asset 2")

        response = self.client.get(
            get_embeddedasset_by_project_endpoint(project.id), secure=True
        )
        data = response.data

        self.assertEquals(len(data), 2)
        self.assertEquals(data[0]["title"], "Asset 2")
        self.assertEquals(data[1]["title"], "Asset 1")

        project.delete()
