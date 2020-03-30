"""bbncreative URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls import url, include
from django.contrib.auth.models import User
from bbncreative_cms.models import Project
from rest_framework import routers, serializers, viewsets

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # Public website
    path("", include("bbncreative_cms.urls")),
    # API URLs
    path("api/", include("bbncreative_api.urls")),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
