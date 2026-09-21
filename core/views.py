from django.http import JsonResponse
from django.shortcuts import render
from django.utils import timezone


def index(request):
    return render(request, "index.html")


def api_info(request):
    # Detrás de Nginx, REMOTE_ADDR es 127.0.0.1; la IP real llega en X-Real-IP
    client_ip = request.META.get("HTTP_X_REAL_IP", request.META.get("REMOTE_ADDR"))

    data = {
        "team": "Equipo 1",
        "members": ["Fredy"],
        "web_server": "Nginx",
        "stack": "Python + Django + Gunicorn",
        "server_time": timezone.localtime().strftime("%d/%m/%Y %H:%M:%S"),
        "client_ip": client_ip,
    }
    return JsonResponse(data)
