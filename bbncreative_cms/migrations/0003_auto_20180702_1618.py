# Generated by Django 2.0.6 on 2018-07-02 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbncreative_cms', '0002_auto_20180702_1617'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Asset Title', max_length=255)),
                ('body', models.TextField(default='Asset Body Text', max_length=5000)),
                ('importance', models.PositiveSmallIntegerField(default=0, unique=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbncreative_cms.Project')),
            ],
            options={
                'ordering': ['importance'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='imageasset',
            name='img',
            field=models.ImageField(max_length=255, upload_to='c21a48da-3d64-4d3a-9021-2df81421cbaa/'),
        ),
    ]
