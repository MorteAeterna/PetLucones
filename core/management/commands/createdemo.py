from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Crea el usuario demo para el proyecto Petlucones."

    def handle(self, *args, **options):
        User = get_user_model()

        username = "user"
        password = "user1234"

        if User.objects.filter(username=username).exists():
            self.stdout.write(
                self.style.WARNING("El usuario demo ya existe.")
            )
            return

        User.objects.create_superuser(
            username=username,
            email="",
            password=password,
        )

        self.stdout.write(
            self.style.SUCCESS("Usuario demo creado correctamente.")
        )