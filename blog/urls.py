from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [

    #localhost:8000/blog/index
    path('', views.home),
    path('index/', views.index),
    path('aboutus/', views.aboutUs),
    path('contactus/', views.contactUs),
    path('feedback/', views.feedback),

]