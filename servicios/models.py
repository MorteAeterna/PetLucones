from django.db import models


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)

    descripcion = models.TextField(
        blank=True
    )

    duracion = models.PositiveIntegerField(
        help_text="Duración en minutos"
    )

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre