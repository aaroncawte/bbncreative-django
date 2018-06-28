from django.contrib import admin

from .models import Project, Collaborator, Credit, ImageAsset, EmbeddedAsset

# Register your models here.
admin.site.register(Project)
admin.site.register(Collaborator)
admin.site.register(Credit)
admin.site.register(ImageAsset)
admin.site.register(EmbeddedAsset)
