# main/views.py
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
import mercadopago

def index(request):
    api_key = 'aff9b828ec6ea97b524645a8dc9ad774'  # Reemplaza esto con tu clave API
    city = 'Quillota'  # Ciudad para la que se va a obtener el clima
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Arrojará un error si la solicitud no fue exitosa
        weather_data = response.json()
        
        context = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon']
        }
    except requests.exceptions.RequestException as e:
        context = {
            'city': city,
            'temperature': 'N/A',
            'description': 'N/A',
            'icon': None,
            'error': f"Error fetching weather data: {e}"
        }

    return render(request, 'index.html', context)

def ingresar(request):
    return render(request, 'ingresar.html')

def checkout(request):
    sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)

    preference_data = {
        "items": [
            {
                "title": "Test Product",
                "quantity": 1,
                "unit_price": 100.0,
            }
        ],
        "back_urls": {
            "success": request.build_absolute_uri('/pago-exitoso/'),
            "failure": request.build_absolute_uri('/pago-fallido/'),
            "pending": request.build_absolute_uri('/pago-pendiente/'),
        },
        "auto_return": "approved",
    }

    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]

    return render(request, 'checkout.html', {
        'preference_id': preference['id']
    })


def pago_exitoso(request):
    return render(request, 'pago_exitoso.html')

def pago_fallido(request):
    return render(request, 'pago_fallido.html')

def pago_pendiente(request):
    return render(request, 'pago_pendiente.html')
