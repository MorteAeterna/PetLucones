from datetime import date, timedelta, time
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone

from clientes.models import Cliente
from mascotas.models import Mascota
from reservas.models import Reserva
from servicios.models import Servicio


class Command(BaseCommand):
    help = "Crea datos demo para Petlucones."

    def handle(self, *args, **options):
        self.crear_usuario()
        self.crear_servicios()
        self.crear_clientes_mascotas()
        self.crear_reservas()

        self.stdout.write(
            self.style.SUCCESS("Datos demo verificados correctamente.")
        )

    def crear_usuario(self):
        User = get_user_model()

        if not User.objects.filter(username="user").exists():
            User.objects.create_superuser(
                username="user",
                email="",
                password="user1234",
            )
            self.stdout.write(self.style.SUCCESS("Usuario demo creado."))
        else:
            self.stdout.write(self.style.WARNING("El usuario demo ya existe."))

    def crear_servicios(self):
        servicios = [
            ("Baño Higiénico", "Limpieza básica con shampoo especializado, secado y perfume.", 45, 12000),
            ("Baño Completo", "Baño profundo con shampoo, acondicionador, secado y cepillado.", 60, 18000),
            ("Corte de Pelo", "Corte de raza o personalizado según las indicaciones del cliente.", 90, 22000),
            ("Baño + Corte", "Servicio completo que incluye baño, secado, cepillado y corte de pelo.", 120, 30000),
            ("Corte de Uñas", "Corte y revisión del estado de las uñas.", 15, 5000),
            ("Limpieza de Oídos", "Limpieza preventiva con productos especializados.", 20, 6000),
            ("Cepillado y Deslanado", "Eliminación de pelo muerto y desenredado del pelaje.", 45, 15000),
            ("Spa Canino Premium", "Incluye baño premium, mascarilla hidratante, corte, limpieza de oídos, corte de uñas y perfume.", 120, 38000),
        ]

        for nombre, descripcion, duracion, precio in servicios:
            Servicio.objects.get_or_create(
                nombre=nombre,
                defaults={
                    "descripcion": descripcion,
                    "duracion": duracion,
                    "precio": Decimal(precio),
                    "activo": True,
                },
            )

    def crear_clientes_mascotas(self):
        datos = [
            {
                "cliente": ("Camila", "Torres", "987654321", "camila.torres@example.com"),
                "mascota": ("Luna", "Perro", "Poodle", date(2021, 5, 12), "Mediano", "Mascota tranquila."),
                "peso": Decimal("8.50"),
            },
            {
                "cliente": ("Matías", "Rojas", "912345678", "matias.rojas@example.com"),
                "mascota": ("Rocky", "Perro", "Bulldog Francés", date(2020, 9, 3), "Pequeño", "No usar perfume."),
                "peso": Decimal("11.20"),
            },
            {
                "cliente": ("Valentina", "Muñoz", "976543210", "valentina.munoz@example.com"),
                "mascota": ("Max", "Perro", "Golden Retriever", date(2019, 2, 20), "Grande", "Requiere cepillado adicional."),
                "peso": Decimal("28.00"),
            },
        ]

        for item in datos:
            nombre, apellido, telefono, correo = item["cliente"]

            cliente, _ = Cliente.objects.get_or_create(
                correo=correo,
                defaults={
                    "nombre": nombre,
                    "apellido": apellido,
                    "telefono": telefono,
                },
            )

            nombre_mascota, especie, raza, nacimiento, tamano, observaciones = item["mascota"]

            Mascota.objects.get_or_create(
                cliente=cliente,
                nombre=nombre_mascota,
                defaults={
                    "especie": especie,
                    "raza": raza,
                    "fecha_nacimiento": nacimiento,
                    "peso": item["peso"],
                    "tamano": tamano,
                    "observaciones": observaciones,
                },
            )

    def crear_reservas(self):
        if Reserva.objects.exists():
            return

        fecha = timezone.localdate()

        while fecha.weekday() == 6:
            fecha += timedelta(days=1)

        servicios = list(Servicio.objects.all())
        mascotas = list(Mascota.objects.all())

        if not servicios or not mascotas:
            return

        reservas = [
            (mascotas[0], servicios[0], fecha, time(10, 0), Reserva.Estado.CONFIRMADA),
            (mascotas[1], servicios[3], fecha, time(12, 0), Reserva.Estado.PENDIENTE),
            (mascotas[2], servicios[2], fecha + timedelta(days=1), time(15, 0), Reserva.Estado.CONFIRMADA),
        ]

        for mascota, servicio, fecha_reserva, hora, estado in reservas:
            Reserva.objects.get_or_create(
                mascota=mascota,
                fecha=fecha_reserva,
                hora=hora,
                defaults={
                    "servicio": servicio,
                    "estado": estado,
                    "observaciones": "Reserva de demostración.",
                },
            )