from django.shortcuts import render, redirect, get_object_or_404

from images.forms import ImageCreate, ImageEdit
from images.models import Image
from images.utils import resize_img


def index(request):
    set_images = Image.objects.all()
    img_list = "Список изображений"
    img_add = "Добавить изображение"
    img_not_found = "Нет доступных изображений"
    return render(
        request,
        "index.html",
        {
            "set_images": set_images,
            "img_list": img_list,
            "img_add": img_add,
            "img_not_found": img_not_found,
        },
    )


def image_create(request):
    img_new = "Новое изображение"
    back_list = "Назад к списку"
    form = ImageCreate(request.POST or None, files=request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            link = form.cleaned_data.get("image_link")
            file = form.cleaned_data.get("image_file")
            # Если image_link существует, сплитим, берем последний элемент - имя понадобится для сохранения в БД
            if link:
                img_name = link.split("/")[-1]  # сплитит через запятую и берем последнее значение
            else:
                img_name = file.name
            # создаем объект класса иммидж
            img_instance = Image()
            img_instance.image.save(img_name, file)
            return redirect("image_edit", id=img_instance.id)

    return render(
        request,
        "image_create.html",
        {
            "form": form,
            "img_new": img_new,
            "back_list": back_list,
        },
    )


def image_edit(request, id):
    back_list = "Назад к списку"
    instance = get_object_or_404(Image, id=id)

    if instance.width or instance.height:
        resize_image = resize_img(
            image=instance.image, width=instance.width, height=instance.height
        )
    else:
        resize_image = instance.image
    form = ImageEdit(request.POST or None, instance=instance)

    if request.method == "POST":
        if form.is_valid():
            instance = form.save()
            return redirect("image_edit", id=instance.id)
    return render(
        request,
        "image_edit.html",
        {
            "form": form,
            "image": resize_image,
            "instance": instance,
            "back_list": back_list,
        },
    )
