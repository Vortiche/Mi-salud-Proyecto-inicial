from django.contrib import admin
from .models import Paciente, Profesional, Reserva

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Profesional)
admin.site.register(Reserva)