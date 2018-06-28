from django.contrib import messages
from django.db import DataError
from django.shortcuts import render, redirect

from bbncreative_cms.models import Project, ImageAsset


def index(request):
    return render(
        request,
        "index.html",
        {}
    )


def projects(request):
    all_projects = Project.objects.all()
    return render(
        request,
        "projects.html",
        {
            'projects': all_projects
        }
    )


def project_from_name(request, url_name):
    results = Project.objects.all().filter(url_name=url_name)

    if results.count() == 0:
        messages.add_message(request, messages.ERROR, "There is no project called " + url_name + ".")
        return redirect('projects')

    if results.count() > 1:
        raise DataError("Multiple projects with the same url_name")

    this_project = results.first()

    return render(
        request,
        "project.html",
        {
            'project': this_project
        }
    )


def image_asset(request, url_uuid, file_name):
    results = ImageAsset.objects.filter(img=url_uuid + "/" + file_name)

    if results.count() == 0:
        messages.add_message(request, messages.ERROR, "There is no asset at this URL.")
        return redirect('index')

    if results.count() > 1:
        raise DataError("Multiple assets with the same filename")

    image = results.first()

    return render(
        request,
        "asset.html",
        {
            'image': image
        }
    )
