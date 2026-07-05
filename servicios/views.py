from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import ServicioForm
from .models import Servicio


class ServicioListView(ListView):
    model = Servicio
    template_name = "servicios/lista.html"
    context_object_name = "servicios"


class ServicioCreateView(CreateView):
    model = Servicio
    form_class = ServicioForm
    template_name = "servicios/formulario.html"
    success_url = reverse_lazy("servicios:lista")

    def form_valid(self, form):
        messages.success(
            self.request,
            "El servicio fue registrado correctamente.",
        )
        return super().form_valid(form)


class ServicioUpdateView(UpdateView):
    model = Servicio
    form_class = ServicioForm
    template_name = "servicios/formulario.html"
    success_url = reverse_lazy("servicios:lista")

    def form_valid(self, form):
        messages.success(
            self.request,
            "El servicio fue actualizado correctamente.",
        )
        return super().form_valid(form)


class ServicioDeleteView(DeleteView):
    model = Servicio
    template_name = "servicios/confirmar_eliminar.html"
    success_url = reverse_lazy("servicios:lista")

    def form_valid(self, form):
        messages.success(
            self.request,
            "El servicio fue eliminado correctamente.",
        )
        return super().form_valid(form)