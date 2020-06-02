# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-04 20:47


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ('mainsite', '0008_auto_20170711_1326'),
        ('oauth2_provider', '0005_auto_20170514_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
