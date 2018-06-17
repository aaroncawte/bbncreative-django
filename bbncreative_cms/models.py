from django.db import models


class Project(models.Model):
    name = models.CharField(
        default="New Project",
        max_length=255
    )


class Collaborator(models.Model):
    # Collaborator's name e.g. "Aaron Cawte"
    name = models.CharField(
        default="Collaborator Name",
        max_length=255
    )
    # Optional collaborator URLs
    url = models.URLField()
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
