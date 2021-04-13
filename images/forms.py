from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Image
from .utils import fetch_image


class ImageCreate(forms.Form):
    image_link = forms.URLField(label="Ссылка", required=False,)
    image_file = forms.ImageField(label="Файл", required=False,)

    def clean(self):
        """
        Реализуем метод Form.clean() когда необходимо добавить кастомную валидацию
        В рамках данной проверки, переопределяем метод clean() класса forms.Form
        - Выбрасывает ValueError в случае если изображения нет или указаны оба варианта: Файл и url
        - Если указан только url,
        - Скачиваем изображение, присваивая его в img_file
        """
        # Родительский метод super().clean() вернет self.cleaned_data
        clean_data = super().clean()

         # Получаем из словаря cleaned_data нужные поля
        img_link = clean_data.get("image_link")
        img_file = clean_data.get("image_file")

        # Проводим собственную валидацию
        if img_link and img_file:
            raise ValidationError("Заполните только одно поле.")

        elif not img_link and not img_file:
            raise ValidationError("А кто поле будет заполнять, Пушкин?")

        elif img_link:
            # Если присутствует url в финальный словарь cleaned_data помещаем его в image_file
            img_file = fetch_image(img_link)
            clean_data["image_file"] = img_file

        return clean_data


class ImageEdit(ModelForm):
    class Meta:
        model = Image
        fields = ("width", "height")
