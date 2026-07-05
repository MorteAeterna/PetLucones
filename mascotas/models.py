from django.db import models
from clientes.models import Cliente


class Mascota(models.Model):

    class Especie(models.TextChoices):
        PERRO = "Perro", "Perro"
        GATO = "Gato", "Gato"

    class Tamano(models.TextChoices):
        PEQUENO = "Pequeño", "Pequeño"
        MEDIANO = "Mediano", "Mediano"
        GRANDE = "Grande", "Grande"

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="mascotas"
    )

    nombre = models.CharField(max_length=100)

    especie = models.CharField(
        max_length=20,
        choices=Especie.choices,
        default=Especie.PERRO
    )

    raza = models.CharField(max_length=100)

    fecha_nacimiento = models.DateField()

    peso = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    tamano = models.CharField(
        max_length=20,
        choices=Tamano.choices
    )

    observaciones = models.TextField(
        blank=True
    )

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre