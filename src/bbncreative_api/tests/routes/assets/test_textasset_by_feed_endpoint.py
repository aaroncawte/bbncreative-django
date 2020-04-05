from rest_framework.test import APITestCase, APIClient
from bbncreative_cms.models import Feed, Project, TextAsset


def get_textasset_by_feed_endpoint(feed_id):
    return "/api/feed/" + str(feed_id) + "/assets/text/"


class TextAssetByFeedEndpointTests(APITestCase):

    client = APIClient()

    def test_textasset_by_feed_endpoint_for_feed_with_no_textassets(self):
        feed = Feed.objects.create()

        response = self.client.get(get_textasset_by_feed_endpoint(feed.id), secure=True)
        data = response.data

        self.assertEquals(len(data), 0)

        feed.delete()

    def test_textasset_by_feed_endpoint_for_feed_with_two_textassets(self):
        project = Project.objects.create(name="Required parent for assets")
        feed = Feed.objects.create()

        asset1 = TextAsset.objects.create(parent=project, title="Asset")
        asset2 = TextAsset.objects.create(parent=project, title="Asset 2")

        asset1.feeds.add(feed)
        asset2.feeds.add(feed)

        response = self.client.get(get_textasset_by_feed_endpoint(feed.id), secure=True)
        data = response.data

        self.assertEquals(data[0]["title"], "Asset 2")
        self.assertEquals(data[1]["title"], "Asset")

        feed.delete()
        project.delete()

    def test_textasset_by_feed_endpoint_for_importance_sorting(self):

        project = Project.objects.create(name="Required parent for assets")
        feed = Feed.objects.create()

        asset1 = TextAsset.objects.create(parent=project, title="Asset", importance=0)
        asset2 = TextAsset.objects.create(parent=project, title="Asset 6", importance=6)

        asset1.feeds.add(feed)
        asset2.feeds.add(feed)

        response = self.client.get(get_textasset_by_feed_endpoint(feed.id), secure=True)
        data = response.data

        self.assertEquals(data[0]["title"], "Asset")
        self.assertEquals(data[1]["title"], "Asset 6")

        feed.delete()
        project.delete()
