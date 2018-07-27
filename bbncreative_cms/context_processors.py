from .models import Project, Feed

NUM_TOP_PROJECTS = 3
NUM_TOP_FEEDS = 3


def top_projects(context):
    projects = Project.objects.order_by('-date_complete')[:NUM_TOP_PROJECTS]
    return {'top_projects': projects}


def top_feeds(context):
    feeds = Feed.objects.filter(protected=False)[:NUM_TOP_FEEDS]
    return {'top_feeds': feeds}
