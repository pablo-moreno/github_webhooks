# Generated by Django 2.2.3 on 2019-07-09 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_auto_20190709_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deploy',
            name='webhook',
        ),
    ]
