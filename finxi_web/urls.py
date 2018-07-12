from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register-customer/", views.create_customer, name="create_customer"),
    path("register-seller/", views.create_seller, name="create_seller"),
    path("register-house/", views.create_house, name="create_house"),
    path("login/", auth_views.login, name="login"),
    path("logout/", auth_views.logout, {"next_page": ""}, name="logout"),
    path("house/<int:house_id>/", views.house_detail, name="house_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
