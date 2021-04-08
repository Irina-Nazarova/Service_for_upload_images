from django import forms


def validate_fields_link(image_link):
    """ Проверка на корректную ссылку."""


def validate_fields_forms(image_link, image_file):
    if image_link and image_file:
        raise forms.ValidationError("Заполните только одно поле.")
    elif not image_link and not image_file:
        raise forms.ValidationError("А кто поле будет заполнять, Пушкин?")

