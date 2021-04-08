from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='',
                                   blank=True,
                                   null=True,
                                   verbose_name='Файл изображения', )
    width = models.IntegerField(
        blank=True, null=True,
        validators=[MinValueValidator(limit_value=0),
                    MaxValueValidator(limit_value=5000,
                                      message="Максимально возможная ширина - 5000", )],
        verbose_name='Ширина')
    height = models.IntegerField(
        blank=True, null=True,
        validators=[MinValueValidator(limit_value=0),
                    MaxValueValidator(limit_value=5000,
                                      message="Максимально возможная высота - 5000", )],
        verbose_name='Высота')

    def __str__(self):
        return f"{self.image}"
