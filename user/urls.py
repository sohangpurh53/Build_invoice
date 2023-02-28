from django.urls import path
from user import views

urlpatterns = [
    path('SignIn/', views.SignIn, name='SignIn'),
    path('SignOut/', views.SignOut, name='SignOut'),
    path('SignUp/', views.SignUp, name='SignUp'),
]
