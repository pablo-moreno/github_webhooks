# Generated by Django 2.2.3 on 2019-07-09 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='github_name',
            new_name='repository',
        ),
        migrations.CreateModel(
            name='WebHook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Application')),
            ],
        ),
    ]
