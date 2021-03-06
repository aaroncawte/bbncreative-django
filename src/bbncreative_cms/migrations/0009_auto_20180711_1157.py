# Generated by Django 2.0.6 on 2018-07-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbncreative_cms', '0008_auto_20180705_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Feed', max_length=255)),
                ('bio', models.TextField(default='Feed Bio', max_length=5000)),
                ('url_name', models.SlugField(allow_unicode=True, default='new-feed', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='embeddedasset',
            name='feeds',
            field=models.ManyToManyField(to='bbncreative_cms.Feed'),
        ),
        migrations.AddField(
            model_name='imageasset',
            name='feeds',
            field=models.ManyToManyField(to='bbncreative_cms.Feed'),
        ),
        migrations.AddField(
            model_name='textasset',
            name='feeds',
            field=models.ManyToManyField(to='bbncreative_cms.Feed'),
        ),
    ]
