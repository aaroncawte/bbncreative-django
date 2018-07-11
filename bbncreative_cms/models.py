import datetime

from django.db import models


def get_file_path(instance, filename):
    import uuid
    newname = str(uuid.uuid4()) + "/" + filename
    return newname


class Project(models.Model):
    name = models.CharField(
        default="New Project",
        max_length=255
    )
    bio = models.TextField(
        max_length=5000,
        default="Project Bio"
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
    cta_title = models.CharField(
        max_length=50,
        default="Go to Website"
    )
    cta_url = models.URLField(
        max_length=255,
        default="https://bbncreative.co"

    )
    client_name = models.CharField(
        max_length=200,
        default="New Client"
    )
    icon = models.ImageField(
        upload_to=get_file_path,
        max_length=255,
        blank=True
    )
    hero = models.ImageField(
        upload_to=get_file_path,
        max_length=255,
        blank=True
    )

    class Meta:
        ordering = ['date_complete', '-is_complete']

    def get_assets(self):
        return Asset.objects.filter(parent=self)

    def __str__(self):
        return self.name + " is a project for " + self.client_name + "."


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

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.project.name + " - " + self.collaborator.name


class Asset(models.Model):
    parent = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=255,
        default="Asset Title"
    )
    body = models.TextField(
        max_length=5000,
        default="Asset Body Text"
    )
    importance = models.PositiveSmallIntegerField(
        default=0
    )

    class Meta:
        abstract = True,
        ordering = ['importance']

    def __str__(self):
        return self.title + " from project: " + self.parent.name


class TextAsset(Asset):
    def __str__(self):
        return self.title + " from project " + self.parent.name

class ImageAsset(Asset):
    alt = models.CharField(
        max_length=255
    )
    img = models.ImageField(
        upload_to=get_file_path,
        max_length=255,
    )


class EmbeddedAsset(Asset):
    embed_code = models.TextField(
        max_length=5000
    )
