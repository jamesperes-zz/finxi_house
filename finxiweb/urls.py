from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register-customer/', views.create_customer, name='create_customer'),
    path('register-seller/', views.create_seller, name='create_seller'),
    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, {'next_page': ''}, name='logout'),
]