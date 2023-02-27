from django.contrib import admin
from django.urls import path, include
from user import views

urlpatterns = [
            path('', views.index, name='index'),
            path('welcome/', views.welcome, name="welcome")
]
