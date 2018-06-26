from django.db import models
import datetime


class Project(models.Model):
    name = models.CharField(
        default="New Project",
        max_length=255
    )
    url_name = models.SlugField(
        max_length=255,
        default="new-project",
        allow_unicode=True
    )
    date_complete = models.DateField(
        auto_now=False,
        auto_now_add=False,
        default=datetime.date.today
    )
    is_complete = models.BooleanField(
        default=False
    )
    project_url = models.URLField(
        max_length=255,
        default="https://bbncreative.co"

    )
    client_name = models.CharField(
        max_length=200,
        default="New Client"
    )


class Collaborator(models.Model):
    # Collaborator's name e.g. "Aaron Cawte"
    name = models.CharField(
        default="Collaborator Name",
        max_length=255
    )
    # Optional collaborator URLs
    url = models.URLField(
        max_length=255
    )
    twitter = models.CharField(
        default="",
        max_length=15
    )


class Credit(models.Model):
    # A credit credits a collaborator for something
    collaborator = models.ForeignKey(
        Collaborator,
        on_delete=models.PROTECT
    )
    # A credit is specific to a project
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    # A credit credits a collaborator for some action
    action = models.CharField(
        default="",
        max_length=255
    )


class Asset(models.Model):
    parent = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    title = models.TextField(
        max_length=255
    )
    body = models.TextField(
        max_length=5000
    )


class ImageAsset(Asset):
    alt=models.TextField(
        max_length=5000
    )
    img=models.FileField(
        upload_to='media/%Y/%m/%d',
        max_length=255,
    )


class EmbeddedAsset(Asset):
    embed_code=models.TextField(
        max_length=5000
    )
