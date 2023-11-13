from django.shortcuts import render, HttpResponse
import serial
import time

# Create your views here.


def home(request):
    try:
        ser = serial.Serial('COM9', 9600)  # Ajusta el puerto según tu configuración
    except:
        print("No se pudo abrir el puerto serial")
    else:
        time.sleep(1)
        ser.write(b'1')  # Envía un byte para encender la luz
        print('portada')
        ser.close()
    finally:
        return render(request, "core/home.html")
    

def about(request):
    try:
        ser = serial.Serial('COM9', 9600)  # Ajusta el puerto según tu configuración
    except:
        print("No se pudo abrir el puerto serial")
    else:
        time.sleep(1)
        ser.write(b'2')  # Envía un byte para encender la luz
        print('acerca')
        ser.close()
    finally:
        return render(request, "core/about.html")
    

def contact(request):
    try:
        ser = serial.Serial('COM9', 9600)  # Ajusta el puerto según tu configuración
    except:
        print("No se pudo abrir el puerto serial")
    else:
        time.sleep(1)
        ser.write(b'3')  # Envía un byte para encender la luz
        print('contacto')
        ser.close()
    finally:
        return render(request, "core/contact.html")

def portfolio(request):
    try:
        ser = serial.Serial('COM9', 9600)  # Ajusta el puerto según tu configuración
    except:
        print("No se pudo abrir el puerto serial")
    else:
        time.sleep(1)
        ser.write(b'4')  # Envía un byte para encender la luz
        print('portafolio')
        ser.close()
    finally:
        return render(request, "core/portfolio.html")