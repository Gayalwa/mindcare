from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('understanding/', views.understanding, name='understanding'),
    path('resources/', views.resources, name='resources'),
    path('contact/', views.contact, name='contact'),
]
