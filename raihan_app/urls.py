from django.urls import path
from . import views

urlpatterns = [
    path("test", views.index, name="index"),
    path('add/', views.add, name='add'),
    path("home/", views.home, name="home"),
    path("", views.login, name="login")
]