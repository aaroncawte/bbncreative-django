from rest_framework import viewsets
from bbncreative_cms.models import Collaborator, Credit, Feed, Project
from bbncreative_api.serializers import CreditSerializer, FeedSerializer, ProjectSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends: [DjangoFilterBackend]
    filterset_fields = ['is_complete']


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    filter_backends: [DjangoFilterBackend]
    filterset_fields = ['protected', 'permanent']


class CreditViewSet(viewsets.ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer

    def get_queryset(self):
        project_id = self.kwargs['project']

        try:
            Project.objects.get(id=project_id)
            return Credit.objects.filter(project=project_id)

        except Project.DoesNotExist:
            raise Http404("Project does not exist")