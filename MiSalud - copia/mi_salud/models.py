from django.db import models

# Create your models here.
class Paciente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.nombre} ({self.rut})"

class Profesional(models.Model):
    nombre = models.CharField(max_length=100)
    servicio = models.CharField(max_length=100)  # Ejemplo: Medicina General, Pediatría
    sucursal = models.CharField(max_length=100)  # Ejemplo: Centro, Norte
    # Guardaremos los horarios como texto separado por comas, ej: "09:00, 10:00, 11:00"
    horarios_disponibles = models.CharField(max_length=200) 

    def _str_(self):
        return f"{self.nombre} - {self.servicio} ({self.sucursal})"

class Reserva(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    servicio = models.CharField(max_length=100)
    sucursal = models.CharField(max_length=100)
    fecha = models.DateField()
    horario = models.CharField(max_length=10)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Hora de {self.paciente.nombre} con {self.profesional.nombre}"
    