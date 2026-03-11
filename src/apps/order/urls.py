from django.urls import path
from . import views


urlpatterns = [
   path('api/make-sale/', views.make_sale_api, name='make_sale_api'),
]