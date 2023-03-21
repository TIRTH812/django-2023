from django import views
from django.contrib import admin
from django.urls import path,include
from .views import ManagerRegisterView, DeveloperRegisterView, UserLoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('managerregister/',ManagerRegisterView.as_view(),name='managerregister'),
    path('developererregister/',DeveloperRegisterView.as_view(),name='developererregister'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    # path('sendmail/',views.sendMail,name='sendmail'),
]