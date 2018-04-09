from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('email/', views.emailView, name='email'),
    path('success/', views.successView, name='success'),

]
