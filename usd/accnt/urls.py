from django.contrib import admin
from django.urls import path,include
from .views import rt
from .import views

urlpatterns = [
    path('',views.rt)

]