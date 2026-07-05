from decimal import Decimal, InvalidOperation

from django import forms

from .models import Servicio


class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = [
            "nombre",
            "descripcion",
            "duracion",
            "precio",
            "activo",
        ]

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "duracion": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "precio": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: 12000 o 12.000",
                }
            ),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def clean_precio(self):
        precio = str(self.cleaned_data["precio"]).strip()

        precio = precio.replace(".", "")
        precio = precio.replace(",", ".")

        try:
            precio_decimal = Decimal(precio)
        except InvalidOperation:
            raise forms.ValidationError("Ingrese un precio válido.")

        if precio_decimal <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")

        return precio_decimal