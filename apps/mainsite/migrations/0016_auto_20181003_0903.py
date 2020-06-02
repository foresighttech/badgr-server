# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-03 16:03


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authtoken', '0002_auto_20160226_1747'),
        ('oauth2_provider', '0006_auto_20171214_2232'),
        migrations.swappable_dependency(settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ('mainsite', '0015_badgrapp_use_auth_code_exchange'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessTokenProxy',
            fields=[
            ],
            options={
                'verbose_name': 'access token',
                'proxy': True,
                'verbose_name_plural': 'access tokens',
                'indexes': [],
            },
            bases=('oauth2_provider.accesstoken',),
        ),
        migrations.CreateModel(
            name='LegacyTokenProxy',
            fields=[
            ],
            options={
                'verbose_name': 'Legacy token',
                'proxy': True,
                'verbose_name_plural': 'Legacy tokens',
                'indexes': [],
            },
            bases=('authtoken.token',),
        ),
        migrations.AddField(
            model_name='badgrapp',
            name='oauth_application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
        ),
    ]
