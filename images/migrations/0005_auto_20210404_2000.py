# Generated by Django 3.1.4 on 2021-04-04 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0004_auto_20210404_1253"),
    ]

    operations = [
        migrations.RenameField(
            model_name="image",
            old_name="image",
            new_name="image_file",
        ),
        migrations.AddField(
            model_name="image",
            name="image_link",
            field=models.URLField(
                default="",
                max_length=2000,
                verbose_name="Cсылка на изображение",
            ),
            preserve_default=False,
        ),
    ]