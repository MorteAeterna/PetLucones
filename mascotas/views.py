from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

from .models import Mascota
from .forms import MascotaForm


class MascotaListView(ListView):
    model = Mascota
    template_name = "mascotas/lista.html"
    context_object_name = "mascotas"
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = Mascota.objects.select_related("cliente").all()

        if query:
            queryset = queryset.filter(
                Q(nombre__icontains=query)
                | Q(raza__icontains=query)
                | Q(cliente__nombre__icontains=query)
                | Q(cliente__apellido__icontains=query)
            )

        return queryset


class MascotaCreateView(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = "mascotas/formulario.html"
    success_url = reverse_lazy("mascotas:lista")

    def form_valid(self, form):
        messages.success(self.request, "La mascota fue registrada correctamente.")
        return super().form_valid(form)


class MascotaUpdateView(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = "mascotas/formulario.html"
    success_url = reverse_lazy("mascotas:lista")

    def form_valid(self, form):
        messages.success(self.request, "Los datos de la mascota fueron actualizados correctamente.")
        return super().form_valid(form)


class MascotaDeleteView(DeleteView):
    model = Mascota
    template_name = "mascotas/confirmar_eliminar.html"
    success_url = reverse_lazy("mascotas:lista")

    def form_valid(self, form):
        messages.success(self.request, "La mascota fue eliminada correctamente.")
        return super().form_valid(form)