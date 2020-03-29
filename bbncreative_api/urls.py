from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from bbncreative_api.view_sets import CreditViewSet, FeedViewSet, ProjectViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'feeds', FeedViewSet)
router.register(r'project/(?P<project>\d+)/credits', CreditViewSet)

urlpatterns = [
    url('', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]
