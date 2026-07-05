from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import ReservaForm
from .models import Reserva


class ReservaListView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = "reservas/lista.html"
    context_object_name = "reservas"
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = Reserva.objects.select_related(
            "mascota",
            "mascota__cliente",
            "servicio",
        ).all()

        if query:
            queryset = queryset.filter(
                Q(mascota__nombre__icontains=query)
                | Q(servicio__nombre__icontains=query)
                | Q(mascota__cliente__nombre__icontains=query)
                | Q(mascota__cliente__apellido__icontains=query)
            )

        return queryset


class ReservaCreateView(LoginRequiredMixin, CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = "reservas/formulario.html"
    success_url = reverse_lazy("reservas:lista")

    def get_initial(self):
        initial = super().get_initial()

        fecha = self.request.GET.get("fecha")
        hora = self.request.GET.get("hora")

        if fecha:
            initial["fecha"] = fecha

        if hora:
            initial["hora"] = hora

        return initial

    def form_valid(self, form):
        messages.success(self.request, "La reserva fue registrada correctamente.")
        return super().form_valid(form)


class ReservaUpdateView(LoginRequiredMixin, UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = "reservas/formulario.html"
    success_url = reverse_lazy("reservas:lista")

    def form_valid(self, form):
        messages.success(self.request, "La reserva fue actualizada correctamente.")
        return super().form_valid(form)


class ReservaDeleteView(LoginRequiredMixin, DeleteView):
    model = Reserva
    template_name = "reservas/confirmar_eliminar.html"
    success_url = reverse_lazy("reservas:lista")

    def form_valid(self, form):
        messages.success(self.request, "La reserva fue eliminada correctamente.")
        return super().form_valid(form)


@login_required
def agenda(request):
    fecha_str = request.GET.get("fecha")
    fecha = timezone.localdate()

    if fecha_str:
        for formato in ["%Y-%m-%d", "%d-%m-%Y"]:
            try:
                fecha = datetime.strptime(fecha_str, formato).date()
                break
            except ValueError:
                continue

    reservas = Reserva.objects.select_related(
        "mascota",
        "mascota__cliente",
        "servicio",
    ).filter(fecha=fecha)

    reservas_por_hora = {
        reserva.hora.strftime("%H:%M"): reserva
        for reserva in reservas
    }

    horas = []

    for hora_num in range(9, 19):
        hora_texto = f"{hora_num:02d}:00"

        horas.append({
            "hora": hora_texto,
            "reserva": reservas_por_hora.get(hora_texto),
        })

    return render(request, "reservas/agenda.html", {
        "fecha": fecha,
        "horas": horas,
    })