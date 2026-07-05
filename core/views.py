from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone

from clientes.models import Cliente
from mascotas.models import Mascota
from servicios.models import Servicio
from reservas.models import Reserva


@login_required
def dashboard(request):
    hoy = timezone.localdate()
    ahora = timezone.localtime().time()

    reservas_del_dia = Reserva.objects.select_related(
        "mascota",
        "mascota__cliente",
        "servicio",
    ).filter(fecha=hoy).order_by("hora")

    proxima_reserva = reservas_del_dia.filter(
        hora__gte=ahora
    ).exclude(
        estado__in=[
            Reserva.Estado.CANCELADA,
            Reserva.Estado.FINALIZADA,
        ]
    ).first()

    ultimas_reservas = Reserva.objects.select_related(
        "mascota",
        "mascota__cliente",
        "servicio",
    ).order_by("-creado")[:5]

    context = {
        "fecha_actual": hoy,
        "total_clientes": Cliente.objects.count(),
        "total_mascotas": Mascota.objects.count(),
        "total_servicios": Servicio.objects.filter(activo=True).count(),
        "reservas_hoy": reservas_del_dia.count(),
        "proxima_reserva": proxima_reserva,
        "reservas_del_dia": reservas_del_dia,
        "ultimas_reservas": ultimas_reservas,
    }

    return render(request, "core/dashboard.html", context)