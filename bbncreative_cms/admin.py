from django.contrib import admin

from .models import Project, Collaborator, Credit, Feed, TextAsset, ImageAsset, EmbeddedAsset

admin.site.site_header = "bbncreative"
admin.site.site_title = "bbncreative CMS"


class CreditInline(admin.TabularInline):
    model = Credit
    extra = 0


class TextAssetInline(admin.StackedInline):
    model = TextAsset
    extra = 0


class ImageAssetInline(admin.StackedInline):
    model = ImageAsset
    extra = 0


class EmbeddedAssetInline(admin.StackedInline):
    model = EmbeddedAsset
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        CreditInline,
        TextAssetInline,
        ImageAssetInline,
        EmbeddedAssetInline,
    ]


class CollaboratorAdmin(admin.ModelAdmin):
    inlines = [
        CreditInline,
    ]


class FeedAdmin(admin.ModelAdmin):
    model = Feed


# Register your models here.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Collaborator, CollaboratorAdmin)
admin.site.register(Feed, FeedAdmin)
admin.site.register(TextAsset)
admin.site.register(ImageAsset)
admin.site.register(EmbeddedAsset)

