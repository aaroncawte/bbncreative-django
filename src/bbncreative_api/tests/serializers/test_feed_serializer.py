import datetime
from django.core.files import File
from django.test import TestCase
from bbncreative_cms.models import Feed
from bbncreative_api.serializers import FeedSerializer
from unittest import mock


class FeedSerializerTests(TestCase):
    def test_feed_serializer_representation(self):
        feed = Feed.objects.create(name="Test Feed")

        representation = FeedSerializer().to_representation(feed)

        self.assertEquals(representation["name"], "Test Feed")
        self.assertEquals(representation["shortName"], "New Feed")
        self.assertEquals(representation["description"], "Feed Bio")
        self.assertEquals(representation["slug"], "new-feed")
        # no sensible test for lastUpdated
        self.assertEquals(representation["icon"]["faName"], "")
        self.assertEquals(representation["protected"], True)
        self.assertEquals(representation["permanent"], False)
        self.assertEquals(representation["images"]["hero"], None)
        self.assertEquals(representation["colors"]["primary"], "e8185f")
        self.assertEquals(representation["colors"]["secondary"], "ff1a36")

        feed.delete()

    def test_customised_feed_serializer_representation(self):
        feed = Feed.objects.create(
            name="Test Feed 2",
            protected=False,
            permanent=True,
            menu_icon_name="test-icon",
        )

        representation = FeedSerializer().to_representation(feed)

        self.assertEquals(representation["name"], "Test Feed 2")
        self.assertEquals(representation["protected"], False)
        self.assertEquals(representation["permanent"], True)
        self.assertEquals(representation["icon"]["faName"], "test-icon")

        feed.delete()

    def test_feed_with_images_serializer_representation(self):

        image_mock = mock.MagicMock(spec=File, name="FileMock")
        image_mock.name = "mocked_img.jpg"

        feed = Feed.objects.create(hero=image_mock)

        representation = FeedSerializer().to_representation(feed)

        self.assertIsNotNone(representation["images"]["hero"][-14:], "mocked_img.jpg")

        feed.delete()
