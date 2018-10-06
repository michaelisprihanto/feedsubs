# Generated by Django 2.1.2 on 2018-10-01 18:53

import django.core.validators
from django.db import migrations, models
import reader.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0010_cachedimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='uri',
            field=models.URLField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='uri',
            field=models.URLField(max_length=2048),
        ),
        migrations.AlterField(
            model_name='cachedimage',
            name='uri',
            field=models.URLField(db_index=True, max_length=2048, unique=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='uri',
            field=models.URLField(max_length=2048, unique=True, validators=[django.core.validators.URLValidator(schemes=['http', 'https']), reader.validators.http_port_validator]),
        ),
    ]