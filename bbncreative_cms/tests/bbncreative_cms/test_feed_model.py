from django.test import TestCase
from django.db.utils import IntegrityError
from bbncreative_cms import models
from django.db import transaction


class FeedModelTests(TestCase):
    def test_feed_url_name_is_unique(self):
        feed_1 = models.Feed.objects.create(name="Existing feed", url_name="same-thing")

        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                models.Feed.objects.create(name="Invading feed", url_name="same-thing")

        feed_1.delete()
