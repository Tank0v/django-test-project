from django.contrib import admin
from .models import Category, Product


# Регистрация моделей в админке
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']  # Параметры для отображения в админке
    prepopulated_fields = {'slug': ('name',)}  # Поля, которые будут заполнены автоматически


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']  # Параметры для фильтрации
    list_editable = ['price', 'available']  # Параметры для изменения
    prepopulated_fields = {'slug': ('name',)}
