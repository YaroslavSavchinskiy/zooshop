from django.shortcuts import render
from .models import Product, Category
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.
def home_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    else:
        products = Product.objects.all()

    products_data = {
        'products': products,
        'categories': categories,
        'query': query,
    }

    return render(request, 'goods/home.html', products_data)

def category_view(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, in_stock=True)

    categories_data = {
        'category': category,
        'products': products,
    }

    return render(request, 'goods/category.html', categories_data)

def product_detail_view(request, slug):
    product = get_object_or_404(Product, slug=slug)

    products_data = {
        'product': product,
    }

    return render(request, 'goods/product_detail.html', products_data)