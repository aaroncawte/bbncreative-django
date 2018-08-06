import json
from urllib import request as urlrequest, parse

from django.conf import settings
from django.contrib import messages
# For the contact form
from django.core.mail import EmailMessage
from django.db import DataError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import get_template

from bbncreative_cms.models import Project, ImageAsset, EmbeddedAsset, TextAsset, Feed, Credit
from .forms import ContactForm


def index(request):
    top_projects = Project.objects.order_by('-date_complete')[:settings.NUM_TOP_PROJECTS]
    top_feeds = Feed.objects.filter(protected=False)[:settings.NUM_TOP_FEEDS]
    return render(
        request,
        "index.html",
        {
            "front_page_projects": top_projects,
            "front_page_feeds": top_feeds,
        }
    )


def aaron(request):
    return render(
        request,
        "aaron.html",
        {
            "page_title": "About Aaron",
            "show_back_to_home": True,
        }
    )


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():

            # reCaptcha Validation
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': os.environ.get("RECAPTCHA_SECRET"),
                'response': recaptcha_response
            }
            data = parse.urlencode(values).encode("utf-8")
            req = urlrequest.Request(url)
            response = urlrequest.urlopen(req, data)
            result = json.load(response)

            # On successful validation
            if result["success"]:
                template = get_template('contact_template.txt')
                context = {
                    'contact_name': form.cleaned_data['name'],
                    'contact_email': form.cleaned_data['email'],
                    'form_content': form.cleaned_data['body'],
                }
                content = template.render(context)

                email = EmailMessage(
                    subject=form.cleaned_data['subject'],
                    body=content,
                    from_email='aaron@bbncreative.co',
                    to=['aaron@bbncreative.co'],
                    reply_to=[form.cleaned_data['email']],
                    headers={'Content-Type': 'text/plain'},
                )
                email.send()

                return HttpResponseRedirect("/contact-thanks")

    #       else:
    #         # return false with reCaptcha error
        # else:
        #     # nothing

    else:
        form = ContactForm()

    return render(
        request,
        "contact.html",
        {
            "page_title": "Get In Touch",
            "show_back_to_home": True,
            "form": form,
            "recaptcha_site_key": os.environ.get("RECAPTCHA_SITE_KEY"),
        }
    )


def contact_thanks(request):
    return render(
        request,
        "contactThanks.html",
        {
            "page_title": "Thank you!",
            "show_back_to_home": True
        }
    )


def privacy(request):
    return render(
        request,
        "privacy.html",
        {
            "page_title": "Privacy Policy",
            "show_back_to_home": True,
        }
    )


def test_page(request):
    return render(
        request,
        "test.html",
        {
            "page_title": "Test Page",
            "show_back_to_home": True,
        }
    )


def projects(request):
    all_projects = Project.objects.all().order_by('date_complete').reverse()

    menu_projects = all_projects
    for p in menu_projects:
        credit_count = Credit.objects.filter(project=p).count()
        p.credit_count = credit_count

    return render(
        request,
        "projects.html",
        {
            'projects': all_projects,
            'globalmenu': menu_projects
        }
    )


def feeds(request):
    all_feeds = Feed.objects.filter(protected=False)
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

    creds = Credit.objects.filter(project=this_project)

    return render(
        request,
        "project.html",
        {
            'project': this_project,
            'assets': my_assets,
            'credits': creds
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
