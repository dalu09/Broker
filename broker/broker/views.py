import requests
from django.http import JsonResponse
import json

def broker_view(request):
    service_url = ""

    if 'servicio1' in request.path:
        #Cambiar ip
        service_url = "http://ip_maquina_servicio1.com/api/endpoint/"

    session = requests.Session()

    try:
        response = session.get(service_url, params=request.GET, timeout=5)  
        return JsonResponse(response.json(), status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": "No se pudo conectar al servicio"}, status=500)

def broker_post(request):
    service_url = ""

    if 'servicio2' in request.path:
        # Assign correct URL for service2
        service_url = "http://ip_maquina_servicio2.com/api/endpoint/"  # Note that this should be service2

    session = requests.Session()

    try:
        # Decode JSON body if available, or use raw data
        json_body = json.loads(request.body.decode('utf-8')) if request.body else {}

        # Forward the POST request with JSON body to the service
        response = session.post(service_url, json=json_body, timeout=5)
        return JsonResponse(response.json(), status=response.status_code)
    except requests.exceptions.RequestException as e:
        # Log the error and return a generic response
        print(f"Error en el request POST: {e}")
        return JsonResponse({"error": "No se pudo conectar al servicio"}, status=500)
