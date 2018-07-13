# Generated by Django 2.0.6 on 2018-07-11 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbncreative_cms', '0009_auto_20180711_1157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='embeddedasset',
            options={'ordering': ['importance', '-created_at']},
        ),
        migrations.AlterModelOptions(
            name='imageasset',
            options={'ordering': ['importance', '-created_at']},
        ),
        migrations.AlterModelOptions(
            name='textasset',
            options={'ordering': ['importance', '-created_at']},
        ),
        migrations.AddField(
            model_name='embeddedasset',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2018-01-01 00:00:00.000+00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imageasset',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2018-01-01 00:00:00.000+00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='textasset',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2018-01-01 00:00:00.000+00'),
            preserve_default=False,
        ),
    ]
