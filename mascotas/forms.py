from django import forms
from .models import Mascota


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = [
            "cliente",
            "nombre",
            "especie",
            "raza",
            "fecha_nacimiento",
            "peso",
            "tamano",
            "observaciones",
        ]

        widgets = {
            "cliente": forms.Select(attrs={"class": "form-control"}),
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "especie": forms.Select(attrs={"class": "form-control"}),
            "raza": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_nacimiento": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "peso": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "tamano": forms.Select(attrs={"class": "form-control"}),
            "observaciones": forms.Textarea(
                attrs={"class": "form-control", "rows": 4}
            ),
        }