from django.contrib import messages
from django.db import DataError
from django.shortcuts import render, redirect

from bbncreative_cms.models import Project, ImageAsset, EmbeddedAsset, TextAsset, Feed


def index(request):
    return render(
        request,
        "index.html",
        {}
    )


def projects(request):
    all_projects = Project.objects.all().order_by('date_complete').reverse()
    return render(
        request,
        "projects.html",
        {
            'projects': all_projects
        }
    )


def feeds(request):
    all_feeds = Feed.objects.all()
    return render(
        request,
        "feeds.html",
        {
            'feeds': all_feeds
        }
    )


class AssetTypes:
    IMAGE = "Image"
    EMBEDDED = "Embedded"
    TEXT = "Text"


def project_from_name(request, url_name):
    results = Project.objects.filter(url_name=url_name)

    if results.count() == 0:
        messages.add_message(request, messages.ERROR, "There is no project called " + url_name + ".")
        return redirect('projects')

    if results.count() > 1:
        raise DataError("Multiple projects with the same url_name")

    this_project = results.first()

    # Get relevant assets from different tables
    image_assets = ImageAsset.objects.filter(parent=this_project)
    embedded_assets = EmbeddedAsset.objects.filter(parent=this_project)
    text_assets = TextAsset.objects.filter(parent=this_project)

    # Add all assets to list and sort by importance
    my_assets = []
    for i in image_assets: my_assets.append((i, AssetTypes.IMAGE, i.importance, i.created_at))
    for e in embedded_assets: my_assets.append((e, AssetTypes.EMBEDDED, e.importance, e.created_at))
    for t in text_assets: my_assets.append((t, AssetTypes.TEXT, t.importance, t.created_at))
    my_assets.sort(key=lambda a: a[3], reverse=True)
    my_assets.sort(key=lambda a: a[2], reverse=False)

    return render(
        request,
        "project.html",
        {
            'project': this_project,
            'assets': my_assets
        }
    )


def feed_from_name(request, url_name):
    results = Feed.objects.filter(url_name=url_name).prefetch_related("embeddedasset_set", "imageasset_set",
                                                                      "textasset_set")

    if results.count() == 0:
        messages.add_message(request, messages.ERROR, "There is no feed called " + url_name + ".")
        return redirect('feeds')

    if results.count() > 1:
        raise DataError("Multiple feeds with the same url_name")

    this_feed = results.first()

    image_assets = this_feed.imageasset_set.all()
    embedded_assets = this_feed.embeddedasset_set.all()
    text_assets = this_feed.textasset_set.all()

    # Add all assets to list and sort by importance
    my_assets = []
    for i in image_assets: my_assets.append((i, AssetTypes.IMAGE, i.created_at))
    for e in embedded_assets: my_assets.append((e, AssetTypes.EMBEDDED, e.created_at))
    for t in text_assets: my_assets.append((t, AssetTypes.TEXT, t.created_at))
    my_assets.sort(key=lambda a: a[2], reverse=True)

    return render(
        request,
        "feed.html",
        {
            'feed': this_feed,
            'assets': my_assets
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
