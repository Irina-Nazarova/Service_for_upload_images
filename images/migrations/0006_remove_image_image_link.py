# Generated by Django 3.1.4 on 2021-04-04 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0005_auto_20210404_2000"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="image",
            name="image_link",
        ),
    ]
