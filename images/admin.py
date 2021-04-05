from django.contrib import admin

from images.models import Image


class ImageAdmin(admin.ModelAdmin):
    image = "__all__"
    empty_value_display = "-пусто-"


admin.site.register(Image, ImageAdmin)
