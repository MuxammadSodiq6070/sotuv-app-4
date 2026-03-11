from django.urls import path
from . import views


urlpatterns = [
    path('monitoring_page/', views.monitoring_page, name="monitoring_page"),
    path('products/', views.products_page, name="products_page"),
    path('products/create/', views.products_create_page, name="products_create_page"),
    path("barcode-scanner/", views.barcode, name="barcode"),
    path('api/get-product/', views.get_product_by_barcode, name='get_product_api'),
    path('pos-sale/', views.pos_sale_view, name='pos_sale_page'),
]