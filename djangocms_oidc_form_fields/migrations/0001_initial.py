# Generated by Django 2.2.13 on 2020-08-11 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='OIDCFieldPlugin',
            fields=[
                ('fieldplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aldryn_forms.FieldPlugin')),
                ('unmodifiable', models.BooleanField(default=True, help_text='The value of the field cannot be changed by the user.', verbose_name='Unmodifiable')),
                ('oidc_attributes', models.CharField(blank=True, help_text='OIDC attributes handovered from provider (names separated by space).', max_length=255, null=True, verbose_name='OIDC attributes')),
            ],
            options={
                'abstract': False,
            },
            bases=('aldryn_forms.fieldplugin',),
        ),
    ]