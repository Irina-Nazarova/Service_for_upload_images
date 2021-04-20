from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase


class TestData(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        image = (
            b"\x47\x49\x46\x38\x39\x61\x02\x00"
            b"\x01\x00\x80\x00\x00\x00\x00\x00"
            b"\xFF\xFF\xFF\x21\xF9\x04\x00\x00"
            b"\x00\x00\x00\x2C\x00\x00\x00\x00"
            b"\x02\x00\x01\x00\x00\x02\x02\x0C"
            b"\x0A\x00\x3B"
        )
        cls.file = SimpleUploadedFile(
            name="img.jpeg", content=image, content_type="image/jpeg"
        )
        cls.link = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"  # noqa
        cls.invalid_link = "https://www.google.com/"


class StaticURLTests(TestData):
    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_page(self):
        response = self.client.get('/create/')
        self.assertEqual(response.status_code, 200)


class TemplatesURLTests(TestData):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client.post("/create/", {"image_file": cls.file}, follow=True)

    def test_urls_correct_template(self):
        templates_url_names = {
            'index.html': '/',
            'image_create.html': '/create/',
            'image_edit.html': '/edit/1/',
        }
        for template, adress in templates_url_names.items():
            with self.subTest(adress=adress):
                response = self.client.get(adress)
                self.assertTemplateUsed(response, template)




