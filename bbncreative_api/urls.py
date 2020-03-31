from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from bbncreative_api.view_sets import (
    CreditViewSet,
    FeedViewSet,
    ProjectViewSet,
    TextAssetViewSet,
    ImageAssetViewSet,
    EmbeddedAssetViewSet,
    FeedTextAssetViewSet,
    FeedImageAssetViewSet,
    FeedEmbeddedAssetViewSet,
)

router = routers.DefaultRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"feeds", FeedViewSet)
router.register(
    r"project/(?P<project>\d+)/credits", CreditViewSet, basename="bbncreative"
)

router.register(
    r"project/(?P<parent>\d+)/assets/text", TextAssetViewSet, basename="bbncreative"
)
router.register(
    r"project/(?P<parent>\d+)/assets/image", ImageAssetViewSet, basename="bbncreative"
)
router.register(
    r"project/(?P<parent>\d+)/assets/embedded",
    EmbeddedAssetViewSet,
    basename="bbncreative",
)

router.register(
    r"feed/(?P<feed_id>\d+)/assets/text", FeedTextAssetViewSet, basename="bbncreative"
)
router.register(
    r"feed/(?P<feed_id>\d+)/assets/image", FeedImageAssetViewSet, basename="bbncreative"
)
router.register(
    r"feed/(?P<feed_id>\d+)/assets/embedded",
    FeedEmbeddedAssetViewSet,
    basename="bbncreative",
)

urlpatterns = [
    url("", include(router.urls)),
    url(r"^auth/", include("rest_framework.urls", namespace="rest_framework")),
]
