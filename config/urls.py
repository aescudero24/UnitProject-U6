from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", homePage, name="home"),   

    path("signup/", signupPage, name="signup"),
    path("login/", loginPage, name="login"),
    path("logout/", logoutPage, name="logout"),

    path('dashboard', adminPage, name="dash"),
    path("pets/", petsPage, name="pets"),
    path("owner/<str:id>", ownerPage, name="owner"),


    path("user/", userPage, name="user"),
    path("settings/", settingsPage, name="settings"),

    path("add-pet/", createPetPage, name="create"),
]
