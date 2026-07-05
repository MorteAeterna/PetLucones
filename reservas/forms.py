from datetime import datetime, time

from django import forms
from django.utils import timezone

from .models import Reserva


HORAS_DISPONIBLES = [
    ("09:00", "09:00"),
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
]


class ReservaForm(forms.ModelForm):
    hora = forms.TypedChoiceField(
        choices=HORAS_DISPONIBLES,
        coerce=lambda value: datetime.strptime(value, "%H:%M").time(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Hora",
    )

    class Meta:
        model = Reserva
        fields = [
            "mascota",
            "servicio",
            "fecha",
            "hora",
            "estado",
            "observaciones",
        ]

        widgets = {
            "mascota": forms.Select(attrs={"class": "form-select"}),
            "servicio": forms.Select(attrs={"class": "form-select"}),
            "fecha": forms.DateInput(
                format="%Y-%m-%d",
                attrs={
                    "class": "form-control",
                    "type": "date",
                },
            ),
            "estado": forms.Select(attrs={"class": "form-select"}),
            "observaciones": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.initial["fecha"] = self.instance.fecha.strftime("%Y-%m-%d")
            self.initial["hora"] = self.instance.hora.strftime("%H:%M")

    def clean_fecha(self):
        fecha = self.cleaned_data["fecha"]
        hoy = timezone.localdate()

        if fecha < hoy:
            raise forms.ValidationError(
                "No se pueden registrar reservas en fechas pasadas."
            )

        if fecha.weekday() == 6:
            raise forms.ValidationError(
                "No se pueden registrar reservas los días domingo."
            )

        return fecha

    def clean_hora(self):
        hora = self.cleaned_data["hora"]

        if hora < time(9, 0) or hora > time(18, 0):
            raise forms.ValidationError(
                "El horario de atención es de 09:00 a 18:00."
            )

        return hora

    def clean(self):
        cleaned_data = super().clean()
        fecha = cleaned_data.get("fecha")
        hora = cleaned_data.get("hora")

        if fecha and hora:
            reserva_existente = Reserva.objects.filter(
                fecha=fecha,
                hora=hora,
            )

            if self.instance.pk:
                reserva_existente = reserva_existente.exclude(
                    pk=self.instance.pk
                )

            if reserva_existente.exists():
                raise forms.ValidationError(
                    "Ya existe una reserva registrada para esa fecha y hora."
                )

        return cleaned_data