from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('projects/', views.projects, name="projects"),
    path('feeds/', views.feeds, name="feeds"),

    path('aaron', views.aaron, name="aaron"),
    path('contact', views.contact, name="contact"),
    path('privacy', views.privacy, name="privacy"),

    path('projects/<slug:url_name>', views.project_from_name, name="project_by_name"),
    path('feeds/<slug:url_name>', views.feed_from_name, name="feed_by_name"),

    path('assets/<slug:url_uuid>/<str:file_name>', views.image_asset, name="image_asset"),

    path('testpage', views.test_page, name="test_page")
]
