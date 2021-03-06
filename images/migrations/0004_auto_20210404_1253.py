# Generated by Django 3.1.4 on 2021-04-04 09:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0003_auto_20210404_1253"),
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
                        limit_value=5000,
                        message="Максимально возможная высота - 5000",
                    ),
                ],
                verbose_name="Высота",
            ),
        ),
    ]
