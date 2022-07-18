from django.db import models

# Create your models here.
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Тэг')
    slug = models.SlugField(max_length=50, verbose_name='url', unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')
    slug = models.SlugField(max_length=50, verbose_name='url', unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class PreviewProduct(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, verbose_name='url', unique=True)
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Тэги')

    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, verbose_name='url', unique=True)
    description = models.TextField(verbose_name='Описание')
    quantity = models.IntegerField(default=0, verbose_name='Количество товаров')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, verbose_name='Миниатюра')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name='Цена')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='Тэги')

    def __str__(self):
        return f'{self.category}: {self.name} -- ${self.price}'

    def get_absolute_url(self):
        return reverse('product', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-views']
