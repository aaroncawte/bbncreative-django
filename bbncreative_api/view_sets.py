from rest_framework import viewsets
from bbncreative_cms.models import (
    Collaborator,
    Credit,
    Feed,
    Project,
    TextAsset,
    ImageAsset,
    EmbeddedAsset,
)
from bbncreative_api.serializers import (
    CreditSerializer,
    FeedSerializer,
    ProjectSerializer,
    TextAssetSerializer,
    ImageAssetSerializer,
    EmbeddedAssetSerializer,
)
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends: [DjangoFilterBackend]
    filterset_fields = ["is_complete"]


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    filter_backends: [DjangoFilterBackend]
    filterset_fields = ["protected", "permanent"]


class CreditViewSet(viewsets.ModelViewSet):
    serializer_class = CreditSerializer

    def get_queryset(self):
        project_id = self.kwargs["project"]

        try:
            Project.objects.get(id=project_id)
            return Credit.objects.filter(project=project_id)

        except Project.DoesNotExist:
            raise Http404("Project does not exist")


class TextAssetViewSet(viewsets.ModelViewSet):
    serializer_class = TextAssetSerializer

    def get_queryset(self):
        parent = self.kwargs["parent"]

        try:
            Project.objects.get(id=parent)
            return TextAsset.objects.filter(parent=parent)

        except Project.DoesNotExist:
            raise Http404("Project does not exist")


class ImageAssetViewSet(viewsets.ModelViewSet):
    serializer_class = ImageAssetSerializer

    def get_queryset(self):
        parent = self.kwargs["parent"]

        try:
            Project.objects.get(id=parent)
            return ImageAsset.objects.filter(parent=parent)

        except Project.DoesNotExist:
            raise Http404("Project does not exist")


class EmbeddedAssetViewSet(viewsets.ModelViewSet):
    serializer_class = EmbeddedAssetSerializer

    def get_queryset(self):
        parent = self.kwargs["parent"]

        try:
            Project.objects.get(id=parent)
            return EmbeddedAsset.objects.filter(parent=parent)

        except Project.DoesNotExist:
            raise Http404("Project does not exist")


class FeedTextAssetViewSet(viewsets.ModelViewSet):
    serializer_class = TextAssetSerializer

    def get_queryset(self):
        feed_id = self.kwargs["feed_id"]

        try:
            Feed.objects.get(id=feed_id)
            return TextAsset.objects.filter(feeds__id__contains=feed_id)

        except Feed.DoesNotExist:
            raise Http404("Feed does not exist")


class FeedImageAssetViewSet(viewsets.ModelViewSet):
    serializer_class = ImageAssetSerializer

    def get_queryset(self):
        feed_id = self.kwargs["feed_id"]

        try:
            Feed.objects.get(id=feed_id)
            return ImageAsset.objects.filter(feeds__id__contains=feed_id)

        except Feed.DoesNotExist:
            raise Http404("Feed does not exist")


class FeedEmbeddedAssetViewSet(viewsets.ModelViewSet):
    serializer_class = EmbeddedAssetSerializer

    def get_queryset(self):
        feed_id = self.kwargs["feed_id"]

        try:
            Feed.objects.get(id=feed_id)
            return EmbeddedAsset.objects.filter(feeds__id__contains=feed_id)

        except Feed.DoesNotExist:
            raise Http404("Feed does not exist")
