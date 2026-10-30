from django.urls import path
from . import views

urlpatterns = [
    path('', views.agendamiento_vista, name='agendamiento'),
]