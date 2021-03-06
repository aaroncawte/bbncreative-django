# Generated by Django 2.0.6 on 2018-07-05 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbncreative_cms', '0006_Project Ordering and Image ID Fix'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_url',
            new_name='cta_url',
        ),
        migrations.AddField(
            model_name='project',
            name='bio',
            field=models.TextField(default='Project Bio', max_length=5000),
        ),
        migrations.AddField(
            model_name='project',
            name='cta_title',
            field=models.CharField(default='Go to Website', max_length=50),
        ),
    ]
