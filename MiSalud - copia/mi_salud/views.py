from django.shortcuts import render
from .models import Paciente, Profesional, Reserva
from datetime import datetime

# Create your views here.
def agendamiento_vista(request):
    # Variables que enviaremos a la pantalla (HTML)
    mensaje_error = None
    mensaje_exito = None
    especialistas_disponibles = None
    
    # Guardamos en variables temporales lo que el usuario va escribiendo
    rut = request.POST.get('rut', '')
    servicio = request.POST.get('servicio', '')
    sucursal = request.POST.get('sucursal', '')
    fecha = request.POST.get('fecha', '')
    horario = request.POST.get('horario', '')

    # PASO 1: Cuando el usuario presiona el primer botón para buscar especialistas
    if request.method == 'POST' and 'buscar' in request.POST:
        # PASO 2: Identificar al paciente en la Base de Datos
        paciente_existe = Paciente.objects.filter(rut=rut).exists()
        
        if not paciente_existe:
            mensaje_error = f"El RUT {rut} no se encuentra registrado en el sistema."
        else:
            # PASO 3: Buscar especialistas con ese servicio y sucursal
            todos_los_profesionales = Profesional.objects.filter(servicio=servicio, sucursal=sucursal)
            
            # Filtramos manualmente los que tengan el bloque horario disponible en su texto
            especialistas_disponibles = []
            for prof in todos_los_profesionales:
                # Convertimos el string "09:00, 10:00" en una lista
                lista_horas = [h.strip() for h in prof.horarios_disponibles.split(',')]
                if horario in lista_horas:
                    especialistas_disponibles.append(prof)
            
            if not especialistas_disponibles:
                mensaje_error = "No existen especialistas disponibles para los criterios buscados."

    # PASO 4, 5 y 6: Cuando el usuario confirma el especialista seleccionado
    elif request.method == 'POST' and 'confirmar' in request.POST:
        profesional_id = request.POST.get('profesional_id')
        profesional = Profesional.objects.get(id=profesional_id)
        paciente = Paciente.objects.get(rut=rut)
        
        # Validar nuevamente que el horario siga libre
        lista_horas = [h.strip() for h in profesional.horarios_disponibles.split(',')]
        if horario in lista_horas:
            # PASO 6: Se asigna el bloque y se crea la Reserva en la BD
            nueva_reserva = Reserva.objects.create(
                paciente=paciente,
                profesional=profesional,
                servicio=servicio,
                sucursal=sucursal,
                fecha=fecha,
                horario=horario
            )
            
            # Quitar el horario del profesional para que no se duplique
            lista_horas.remove(horario)
            profesional.horarios_disponibles = ", ".join(lista_horas)
            profesional.save()
            
            # PASO 7: Éxito observable
            mensaje_exito = f"¡Solicitud completada con éxito! La información fue transferida a la sucursal {sucursal} y al {profesional.nombre}."
        else:
            mensaje_error = "Lo sentimos, el bloque horario ya no se encuentra disponible."

    # Datos que le pasamos al archivo HTML para que aparezcan en pantalla
    contexto = {
        'rut': rut, 'servicio': servicio, 'sucursal': sucursal, 'fecha': fecha, 'horario': horario,
        'mensaje_error': mensaje_error,
        'mensaje_exito': mensaje_exito,
        'especialistas': especialistas_disponibles
    }
    return render(request, 'mi_salud/index.html', contexto)
