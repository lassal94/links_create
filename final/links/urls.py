from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('ssyl', views.links, name='ssyl'),
    path('go_link/<slug>', views.goLink, name='go_link'),
    ]
