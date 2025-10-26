from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


# Функциональные представления
def product_list(request, category_slug=None):
    categories = Category.objects.all()  # Категории для вывода
    products = Product.objects.filter(available=True)  # Продукты для вывода

    category = None
    if category_slug:  # Если есть параметр на фильтрацию
        category = get_object_or_404(Category, slug=category_slug)  # Получаем выбранную категорию из бд
        products = products.filter(category=category)  # Получаем все продукты по выбранной категории

    return render(request,
                  'main/product/list.html',  # Шаблон
                  {'category': category,  # Контекст - то, что выводим
                   'categories': categories,
                   'products': products})


# Страница продукта
def product_detail(request, id, slug):
    # Берём из модели продукт с совпадением id и slug
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    # Похожие продукты (с такой же категорией)
    related_products = Product.objects.filter(category=product.category,
                                              available=True).exclude(id=product.id)[:4]
    cart_product_form = CartAddProductForm()

    return render(request,
                  'main/product/detail.html',
                  {'product': product,
                   'related_products': related_products,
                   'cart_product_form': cart_product_form})
