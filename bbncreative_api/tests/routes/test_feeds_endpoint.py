from rest_framework.test import APITestCase, APIClient
from bbncreative_cms.models import Feed

FEEDS_ENDPOINT = "/api/feeds/"


class FeedEndpointTests(APITestCase):

    client = APIClient()

    def test_feeds_endpoint_with_no_data(self):
        response = self.client.get(FEEDS_ENDPOINT, secure=True)
        data = response.data

        self.assertEquals(len(data), 0)

    def test_feeds_endpoint_with_one_blank_project(self):
        feed = Feed.objects.create(name="Test")

        response = self.client.get(FEEDS_ENDPOINT, secure=True)
        data = response.data

        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]["name"], "Test")
        self.assertTrue(data[0]["protected"])
        self.assertFalse(data[0]["permanent"])

        feed.delete()

    def test_feeds_endpoint_with_three_blank_feeds(self):
        feed1 = Feed.objects.create(name="Test 1", url_name="feed-1")
        feed2 = Feed.objects.create(name="Test 2", url_name="feed-2")
        feed3 = Feed.objects.create(name="Test 3", url_name="feed-3")

        response = self.client.get(FEEDS_ENDPOINT, secure=True)
        data = response.data

        self.assertEquals(len(data), 3)
        # Feeds are presented in reverse chronological order
        self.assertEquals(data[0]["name"], "Test 3")
        self.assertEquals(data[1]["name"], "Test 2")
        self.assertEquals(data[2]["name"], "Test 1")

        feed1.delete()
        feed2.delete()
        feed3.delete()
