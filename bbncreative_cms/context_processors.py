from django.conf import settings

from .models import Project, Feed


def top_projects(context):
    projects = Project.objects.order_by('-date_complete')[:settings.NUM_TOP_PROJECTS]
    return {'top_projects': projects}


def top_feeds(context):
    feeds = Feed.objects.filter(protected=False)[:settings.NUM_TOP_FEEDS]
    return {'top_feeds': feeds}
