# Generated by Django 2.2.17 on 2021-01-14 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_app", "0003_contact_project"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="image_alt",
            field=models.CharField(default=" ", max_length=128),
        ),
    ]
