from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/info/", views.api_info, name="api_info"),
]
