from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('task',views.task,name='task'),
    path('delete',views.delete,name='delete'),
    path('update',views.update,name='update'),
]
