from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard_page, name='dashboard_page'),
    path("creator=Muxammad-Sodiq/alimov/shikoyat-va-takliflar-uchun/phone_number=+998-95-272-60-70/telegram-@Muxammad_Sodiq_60_70/auth/login/", views.login_page, name='login_page'),
    path("creator=Muxammad-Sodiq/alimov/shikoyat-va-takliflar-uchun/phone_number=+998-95-272-60-70/telegram-@Muxammad_Sodiq_60_70/auth/logout/", views.logout_page, name='logout_page')
]