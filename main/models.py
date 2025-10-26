from django.db import models
from django.urls import reverse


# Таблица категорий
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)  # Генерация url в читаемом виде

    class Meta:  # Параметры, с которыми будет работать админка
        ordering = ('name',)  # Сортировка по названию категории
        verbose_name = 'Категория'  # Перевод на русский язык
        verbose_name_plural = 'Категории'  # Параметр отображения во множественном числе

    def __str__(self):  # Отображение
        return self.name

    def get_absolute_url(self):  # Ссылка на продукты из категории
        return reverse("main:product_list_by_category", args=[self.slug])


# Таблица продукта
class Product(models.Model):
    # Наследование от категории (внешний ключ)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=100)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)  # Сортировка по названию категории

    def __str__(self):  # Отображение
        return self.name

    def get_absolute_url(self):  # Ссылка на продукт
        return reverse("main:product_detail", args=[self.id, self.slug])
