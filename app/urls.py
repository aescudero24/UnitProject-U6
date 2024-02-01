from django.urls import path
from .views import *


urlpatterns = [
	
    path("", loginPage, name="login"),

       

    path("signup/", signupPage, name="signup"),
    path("logout/", logoutPage, name="logout"),

    path("home/", homePage, name="home"),
    path('dashboard/', adminPage, name="dash"),
    
    path("pets/", petsPage, name="pets"),
    path("adopt/<str:id>/", adoptionPage, name="adopt"),
    path("owner/<str:id>/", homePage, name="owner"),

    path("settings/", settingsPage, name="settings"),

    path("add-pet/", createPetPage, name="create"),
    path("delete-user/<str:id>/", deleteUserPage, name="delete")
]
