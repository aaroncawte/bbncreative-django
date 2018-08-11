import datetime

from django.db import models


def generate_file_path(instance, filename):
    import uuid
    new_name = str(uuid.uuid4()) + "/" + filename
    return new_name


class Project(models.Model):
    name = models.CharField(
        default="New Project",
        max_length=255
    )
    bio = models.TextField(
        max_length=5000,
        default="Project Bio"
    )
    # Internal URL slug (e.g. /project/slug-field)
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
    # To override date_complete if the project is not complete, when ordering
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
        upload_to=generate_file_path,
        max_length=255,
        blank=True
    )
    hero = models.ImageField(
        upload_to=generate_file_path,
        max_length=255,
        blank=True
    )
    brand_color_1 = models.CharField(
        max_length=6,
        default="455a64"  # blue-grey1
    )
    brand_color_2 = models.CharField(
        max_length=6,
        blank=True
    )

    class Meta:
        ordering = ['date_complete', '-is_complete']

    def get_image_assets(self):
        return ImageAsset.objects.filter(parent=self)

    def get_embedded_assets(self):
        return EmbeddedAsset.objects.filter(parent=self)

    def get_text_assets(self):
        return TextAsset.objects.filter(parent=self)

    def count_assets(self):
        return ImageAsset.objects.filter(parent=self).count() + EmbeddedAsset.objects.filter(parent=self).count() + \
               TextAsset.objects.filter(parent=self).count()

    def count_collaborators(self):
        credits_list = Credit.objects.filter(project=self)
        found_collaborators = set()
        for c in credits_list:
            found_collaborators.add(c.collaborator)
        return len(found_collaborators)

    def __str__(self):
        return self.name + " is a project for " + self.client_name + "."


class Feed(models.Model):
    name = models.CharField(
        default="New Feed",
        max_length=255
    )
    bio = models.TextField(
        max_length=5000,
        default="Feed Bio"
    )
    url_name = models.SlugField(
        max_length=255,
        default="new-feed",
        allow_unicode=True
    )
    menu_icon_name = models.CharField(
        max_length=50,
        blank=True
    )
    protected = models.BooleanField(
        default=True
    )
    hero = models.ImageField(
        upload_to=generate_file_path,
        max_length=255,
        blank=True
    )
    brand_color_1 = models.CharField(
        max_length=6,
        default="455a64"  # blue-grey1
    )
    brand_color_2 = models.CharField(
        max_length=6,
        blank=True
    )

    def __str__(self):
        return self.name + " (" + self.url_name + ")"


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
    # An asset belongs to one project
    parent = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    # Add assets to feeds (e.g. web design)
    feeds = models.ManyToManyField(Feed, blank=True)
    # Creation time for ordering
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    # Every asset has a text-based title
    title = models.CharField(
        max_length=255,
        default="Asset Title"
    )
    # Every asset has a text component (the focus in TextAssets, a description in media assets)
    body = models.TextField(
        max_length=5000,
        default="Asset Body Text"
    )
    # Orders elements on project pages, where 0 is most important and numbers descend
    importance = models.PositiveSmallIntegerField(
        default=0
    )

    class Meta:
        abstract = True,  # TextAsset, ImageAsset and EmbeddedAsset implement this abstraction
        ordering = ['importance', '-created_at']  # See importance comment above

    def __str__(self):
        return self.title + " from project: " + self.parent.name


class TextAsset(Asset):
    # Overridden so the child class isn't empty
    def __str__(self):
        return self.title + " from project " + self.parent.name


class ImageAsset(Asset):
    # Images need alt text
    alt = models.CharField(
        max_length=255
    )
    # Self-explanatory
    img = models.ImageField(
        upload_to=generate_file_path,
        max_length=255,
    )

    def has_media(self):
        if self.img:
            return True
        return False


class EmbeddedAsset(Asset):
    # HTML embed code - will accept any HTML up to 5,000 characters. Be cautious of embed content.
    embed_code = models.TextField(
        max_length=5000
    )

    def has_media(self):
        if len(self.embed_code) > 0:
            return True
        return False
