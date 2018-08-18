from django.conf.urls import url
from . import views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]