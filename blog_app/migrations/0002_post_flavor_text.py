# Generated by Django 2.2.17 on 2021-01-13 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="flavor_text",
            field=models.CharField(default=" ", max_length=128),
        ),
    ]
