from django.db import models
from tinymce.models import HTMLField
from django.core.exceptions import ValidationError


class Post(models.Model):

    STATUS = (
        (0, 'Черновик'),
        (1, 'Опубликовано')
    )

    TYPE = (
        (1, 'Аудиторский отчет'),
        (0, 'Новость')
    )

    title = models.CharField(max_length=200, verbose_name="Заголовок")
    #slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(
        auto_now=True, verbose_name="Дата обнавления")
    content = HTMLField(verbose_name="Описание")
    image = models.ImageField(
        upload_to='services_section', verbose_name="Изображение")
    created_on = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания")
    status = models.IntegerField(
        choices=STATUS, default=0, verbose_name="Статус Поста")
    post_type = models.IntegerField(
        choices=TYPE, default=1, verbose_name="Тип поста")

    class Meta:
        ordering = ['-created_on']
        verbose_name = "Блок: Пост (Новость, Аудиторский отчет)"
        verbose_name_plural = "Блоки: Постов (Новости, Аудиторские отчеты)"

    def __str__(self):
        return f"{self.title} от:{self.created_on} тип:{self.post_type} статус:{self.status}"


class HelloPage(models.Model):
    IMAGE_ALIGIN = (
        (0, 'Слева'),
        (1, 'Справа')
    )

    description = HTMLField(max_length=300, verbose_name="Описание")
    image = models.ImageField(
        upload_to='hello_section', verbose_name="Изображение")
    imageAligin = models.FloatField(
        choices=IMAGE_ALIGIN, default=0, verbose_name="Расположение картинки")

    class Meta:
        verbose_name = "Блок: ООО “СЗУАП-АУДИТ”"
        verbose_name_plural = "Блоки: ООО “СЗУАП-АУДИТ”"

    def __str__(self):
        return f"ООО “СЗУАП-АУДИТ”"


class Service(models.Model):
    label = models.CharField(max_length=300, verbose_name="Заголовок")
    image = models.ImageField(
        upload_to='services_section', verbose_name="Изображение")
    description = HTMLField(max_length=1500, verbose_name="Описание")

    class Meta:
        verbose_name = "Блок: Услуги"
        verbose_name_plural = "Блоки: Услуги"
    def __str__(self):
        return f"{self.label}"


class AboutUs(models.Model):
    # label = models.CharField(max_length=300, verbose_name="Заголовок")
    description = HTMLField(max_length=1500, verbose_name="Описание")

    class Meta:
        verbose_name = "Блок: О нас"
        verbose_name_plural = "О нас"

    def __str__(self):
        return f"О нас"


class Buisness(models.Model):
    # label = models.CharField(max_length=300, verbose_name="Заголовок")
    description = HTMLField(max_length=1500, verbose_name="Описание")

    class Meta:
        verbose_name = "Блок: О деятельности"
        verbose_name_plural = "О деятельности"

    def __str__(self):
        return f"О деятельности"


class Carier(models.Model):
    # label = models.CharField(max_length=300, verbose_name="Заголовок")
    description = HTMLField(max_length=1500, verbose_name="Описание")

    class Meta:
        verbose_name = "Блок: Карьера”"
        verbose_name_plural = "Карьера"

    def __str__(self):
        return f"Карьера"

class Contacts(models.Model):
    description = HTMLField(max_length=1500, verbose_name="Описание")
    class Meta:
        verbose_name = "Блок: Контакты"
        verbose_name_plural = "Контакты"

    def __str__(self):
        return f"Контакты"
