# Generated by Django 2.0.7 on 2018-07-31 12:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bbncreative_cms', '0014_auto_20180731_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embeddedasset',
            name='feeds',
            field=models.ManyToManyField(blank=True, to='bbncreative_cms.Feed'),
        ),
        migrations.AlterField(
            model_name='imageasset',
            name='feeds',
            field=models.ManyToManyField(blank=True, to='bbncreative_cms.Feed'),
        ),
        migrations.AlterField(
            model_name='textasset',
            name='feeds',
            field=models.ManyToManyField(blank=True, to='bbncreative_cms.Feed'),
        ),
    ]