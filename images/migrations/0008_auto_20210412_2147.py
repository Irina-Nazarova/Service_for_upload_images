# Generated by Django 3.1.4 on 2021-04-12 18:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0007_auto_20210405_2233"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="height",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(limit_value=0),
                    django.core.validators.MaxValueValidator(
                        limit_value=4320,
                        message="Максимально возможная высота - 4320",
                    ),
                ],
                verbose_name="Высота",
            ),
        ),
        migrations.AlterField(
            model_name="image",
            name="width",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(limit_value=0),
                    django.core.validators.MaxValueValidator(
                        limit_value=7680,
                        message="Максимально возможная ширина - 7680",
                    ),
                ],
                verbose_name="Ширина",
            ),
        ),
    ]