from django.shortcuts import render, redirect

from images.forms import ImageCreate
from images.models import Image


def index(request):
    set_images = Image.objects.all()
    img_list = "Список изображений"
    img_add = "Добавить изображение"
    img_not_found = "Нет доступных изображений"
    return render(
        request, "index.html", {"set_images": set_images,
                                "img_list": img_list,
                                "img_add": img_add,
                                "img_not_found": img_not_found,},)


def image_create(request):
    pass


def image_edit(request):
    pass
