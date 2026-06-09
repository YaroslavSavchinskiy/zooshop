from django.urls import path
from . import views

app_name = 'goods'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('category/<slug:slug>/', views.category_view, name='category'),
    path('product/<slug:slug>/', views.product_detail_view, name='product_detail'),
]