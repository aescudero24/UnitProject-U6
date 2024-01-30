from django.urls import path
from .views import *


urlpatterns = [
	path("home/", homePage, name="home"),   

    path("signup/", signupPage, name="signup"),
    path("", loginPage, name="login"),
    path("logout/", logoutPage, name="logout"),

    path('dashboard/', adminPage, name="dash"),
    path("pets/", petsPage, name="pets"),
    path("owner/<str:id>/", homePage, name="owner"),


    path("user/", userPage, name="user"),
    path("settings/", settingsPage, name="settings"),

    path("add-pet/", createPetPage, name="create"),
    path("delete", deleteUser, name="deleteUser")

]
