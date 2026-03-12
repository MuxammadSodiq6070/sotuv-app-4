from django.urls import path
from . import views


urlpatterns = [
   path('api/make-sale/', views.sotuv_page, name='sotuv_page'),
]
