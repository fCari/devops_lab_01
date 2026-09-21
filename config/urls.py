from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Incluye todas las rutas de la app 'core' en la raíz del sitio
    path("", include("core.urls")),
]
