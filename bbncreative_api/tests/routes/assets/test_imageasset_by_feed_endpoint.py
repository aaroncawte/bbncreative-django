from rest_framework.test import APITestCase, APIClient
from bbncreative_cms.models import Feed, Project, ImageAsset


def get_imageasset_by_feed_endpoint(project_id):
    return "/api/feed/" + str(project_id) + "/assets/image/"


class ImageAssetByFeedEndpointTests(APITestCase):

    client = APIClient()

    def test_imageasset_by_feed_endpoint_for_project_with_no_imageassets(self):
        feed = Feed.objects.create()

        response = self.client.get(
            get_imageasset_by_feed_endpoint(feed.id), secure=True
        )
        data = response.data

        self.assertEquals(len(data), 0)

        feed.delete()

    def test_imageasset_by_feed_endpoint_for_project_with_two_imageassets(self):
        project = Project.objects.create()
        feed = Feed.objects.create()

        asset1 = ImageAsset.objects.create(parent=project, title="Asset 1")
        asset2 = ImageAsset.objects.create(parent=project, title="Asset 2")

        asset1.feeds.add(feed)
        asset2.feeds.add(feed)

        response = self.client.get(
            get_imageasset_by_feed_endpoint(feed.id), secure=True
        )
        data = response.data

        self.assertEquals(len(data), 2)
        self.assertEquals(data[0]["title"], "Asset 2")
        self.assertEquals(data[1]["title"], "Asset 1")

        feed.delete()
        project.delete()
