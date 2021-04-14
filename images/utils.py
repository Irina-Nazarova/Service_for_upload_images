from PIL import Image as PilImage
from io import BytesIO
from urllib.request import urlopen

from django.core.exceptions import ValidationError
from sorl.thumbnail import get_thumbnail


def resize_img(image, width=None, height=None):
    """ Support format: 1920 x 1080 """
    geometry_string = ""
    if width:
        geometry_string += str(width)
    if height:
        geometry_string += "x" + str(height)
    return get_thumbnail(image, geometry_string, crop="center")


def fetch_image(link):
    try:
        content = BytesIO(urlopen(link).read())
        PilImage.open(content)

    except Exception:
        raise ValidationError("По url не удалось найти изображение.")
    return content
