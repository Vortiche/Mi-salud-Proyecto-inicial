MiSalud - Proyecto Inicial

Este es un prototipo de una aplicacion de agendamiento de horas medicas. los pasos para probar la funcionalidad corazón de esta son:

Requisitos Previos

Python 3.x instalado en tu sistema.

Git (opcional, para clonar el repositorio).

Instrucciones de Instalación y Ejecución Local

Sigue estos pasos en tu terminal (se recomienda usar PowerShell o la terminal de VS Code) para levantar el proyecto en tu computador:

1. Clonar el repositorio y entrar a la carpeta

git clone https://github.com/TuUsuario/Mi-salud-Proyecto-inicial.git
cd "Mi-salud-Proyecto-inicial/MiSalud - copia"


(Nota: Asegúrate de estar posicionado en el directorio que contiene el archivo manage.py)

2. Crear y activar el entorno virtual

python -m venv .venv
.\.venv\Scripts\activate


(Si usas macOS/Linux, el comando de activación es source .venv/bin/activate)

3. Instalar dependencias
El proyecto requiere Django para funcionar.

pip install django


4. Preparar la base de datos
Ejecuta las migraciones para crear las tablas necesarias (Pacientes, Profesionales y Reservas).

python manage.py makemigrations
python manage.py migrate


5. Crear un superusuario (Administrador)
Necesitarás esta cuenta para ingresar los datos de prueba al sistema.

python manage.py createsuperuser


(Sigue las instrucciones en pantalla para definir un usuario y contraseña)

6. Iniciar el servidor de desarrollo

python manage.py runserver


La aplicación estará disponible en tu navegador en: http://127.0.0.1:8000/

Cómo probar la Funcionalidad Corazón (Agendamiento)

Para que el formulario principal funcione, la base de datos necesita tener al menos un paciente registrado y un profesional con horas disponibles. Sigue estos pasos para la prueba de concepto:

Paso A: Cargar datos de prueba

Con el servidor corriendo, entra a http://127.0.0.1:8000/admin/

Inicia sesión con las credenciales del superusuario que creaste en el paso 5.

En la sección Pacientes, haz clic en "Añadir". Ingresa el RUT 12345678-9 y un nombre (ej. "Paciente Prueba"). Guarda los cambios.

En la sección Profesionales, haz clic en "Añadir" y completa exactamente con estos datos:

Nombre: Dr. Prueba

Servicio: Medicina General

Sucursal: Centro

Horarios disponibles: 09:00, 10:00, 11:00
(Los horarios deben ir separados por comas).

Paso B: Simular una reserva

Ve a la página principal de la aplicación web: http://127.0.0.1:8000/

Llena el formulario con los siguientes datos:

RUT: 12345678-9

Servicio: Medicina General

Sucursal: Centro

Fecha: (Elige cualquier fecha en el calendario)

Bloque Horario: 10:00

Presiona "Buscar Especialistas Disponibles". El sistema validará el RUT y encontrará al "Dr. Prueba".

En la lista desplegable que aparecerá, selecciona al doctor y presiona "Confirmar e Inscribir Hora".

Verás un mensaje de éxito color verde indicando que la solicitud fue completada.

Nota sobre la disponibilidad: Si intentas volver a buscar las 10:00 para ese mismo doctor, el sistema te arrojará un error indicando que el bloque ya no está disponible, demostrando que la lógica de prevención de tope de horarios funciona correctamente. Para hacer otra prueba, intenta con las 09:00 o las 11:00.
