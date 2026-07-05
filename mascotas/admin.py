from django.contrib import admin
from .models import Mascota


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "cliente",
        "especie",
        "raza",
        "peso",
        "tamano",
    )

    list_filter = (
        "especie",
        "tamano",
    )

    search_fields = (
        "nombre",
        "cliente__nombre",
        "cliente__apellido",
    )