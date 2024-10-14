import requests
from django.http import JsonResponse

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
        #Cambiar ip
        service_url = "http://ip_maquina_servicio1.com/api/endpoint/"

    session = requests.Session()

    try:
        response = session.get(service_url, params=request.body, timeout=5)  
        return JsonResponse(response.json(), status=response.status_code)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": "No se pudo conectar al servicio"}, status=500)
