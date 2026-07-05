from django.db import models

from mascotas.models import Mascota
from servicios.models import Servicio


class Reserva(models.Model):

    class Estado(models.TextChoices):
        PENDIENTE = "Pendiente", "Pendiente"
        CONFIRMADA = "Confirmada", "Confirmada"
        EN_PROCESO = "En Proceso", "En Proceso"
        FINALIZADA = "Finalizada", "Finalizada"
        CANCELADA = "Cancelada", "Cancelada"

    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name="reservas"
    )

    servicio = models.ForeignKey(
        Servicio,
        on_delete=models.PROTECT,
        related_name="reservas"
    )

    fecha = models.DateField()
    hora = models.TimeField()

    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.PENDIENTE
    )

    observaciones = models.TextField(blank=True)

    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["fecha", "hora"]

    def __str__(self):
        return f"{self.mascota} - {self.fecha} {self.hora}"

    def estado_clase(self):
        clases = {
            self.Estado.PENDIENTE: "badge-estado-pendiente",
            self.Estado.CONFIRMADA: "badge-estado-confirmada",
            self.Estado.EN_PROCESO: "badge-estado-proceso",
            self.Estado.FINALIZADA: "badge-estado-finalizada",
            self.Estado.CANCELADA: "badge-estado-cancelada",
        }

        return clases.get(self.estado, "badge-estado-default")