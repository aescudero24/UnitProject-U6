from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboardPage, name="dash"),
    path("home/", homePage, name="home"),
    path("accounts/login/", loginPage, name="login"),
    path("accounts/signup/", signupPage, name="signup"),
    path("accounts/pets/", pets, name="pets"),
    path("accounts/admin_settings/", adminPage, name="admin_settings"),
    path("accounts/create/", create, name="create"),
    path("logout/", logoutPage, name="logout"),
]
