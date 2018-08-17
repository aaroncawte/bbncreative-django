from django.urls import path

from bbncreative_cms.views import views, views_static, views_contact

urlpatterns = [
    path('', views.index, name="index"),
    path('projects/', views.projects, name="projects"),
    path('feeds/', views.feeds, name="feeds"),

    path('projects/<slug:url_name>', views.project_from_name, name="project_by_name"),
    path('feeds/<slug:url_name>', views.feed_from_name, name="feed_by_name"),

    path('assets/<slug:url_uuid>/<str:file_name>', views.image_asset, name="image_asset"),

    # Contact pages
    path('contact', views_contact.contact, name="contact"),
    path('contact-thanks', views_contact.contact_thanks, name="contact-thanks"),

    #  Static pages
    path('aaron', views_static.aaron, name="aaron"),
    path('privacy', views_static.privacy, name="privacy")
]
