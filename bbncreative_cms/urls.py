from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('projects/', views.projects, name="projects"),

    path('projects/<slug:url_name>', views.project_from_name, name="project_by_name"),

    path('assets/<slug:url_uuid>/<str:file_name>', views.image_asset, name="image_asset")
]
