from django import forms
from django.forms import ModelForm

from .models import Image


class ImageCreate(forms.Form):
    image_link = forms.URLField(label='Ссылка', required=False)
    image_file = forms.ImageField(label='Файл', required=False)


class ImageEdit(ModelForm):
    class Meta:
        model = Image
        fields = ('width', 'height')


