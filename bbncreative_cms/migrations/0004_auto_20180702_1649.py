# Generated by Django 2.0.6 on 2018-07-02 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbncreative_cms', '0003_auto_20180702_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='embeddedasset',
            name='importance',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='imageasset',
            name='img',
            field=models.ImageField(max_length=255, upload_to='8349b5ff-5dae-4ade-9200-ff6769bcd4d1/'),
        ),
        migrations.AlterField(
            model_name='imageasset',
            name='importance',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='textasset',
            name='importance',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
