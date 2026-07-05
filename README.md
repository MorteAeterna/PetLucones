PetLucones

Sistema web de gestión para peluquería canina desarrollado con Django, diseñado para administrar clientes, mascotas, servicios y reservas mediante una interfaz moderna e intuitiva.

---

Demo

**Aplicación:**
https://petlucones.onrender.com

### Usuario de prueba

Usuario:
```
user
```

Contraseña:
```
user1234
```

---

Características

- Autenticación de usuarios
- Dashboard con estadísticas
- Gestión de clientes
- Gestión de mascotas
- Administración de servicios
- Agenda diaria de reservas
- Buscador en los módulos principales
- Diseño responsive
- Interfaz moderna con Bootstrap
- Datos de demostración automáticos

---

Tecnologías

- Django 6
- Python 3.13
- Bootstrap 5
- PostgreSQL / SQLite
- Gunicorn
- WhiteNoise
- Render
- Git + GitHub

---

Capturas

Login

<img width="1910" height="911" alt="image" src="https://github.com/user-attachments/assets/99401b59-a258-4959-8f7f-b61b63ab752f" />


---

Dashboard

<img width="1905" height="907" alt="image" src="https://github.com/user-attachments/assets/b4e7f9a7-1480-4fff-ab9e-5718736331f8" />


---

Agenda

<img width="1888" height="909" alt="image" src="https://github.com/user-attachments/assets/ce0c57cd-f44d-4e81-88c3-cca11fefe886" />


---

Clientes

<img width="1908" height="905" alt="image" src="https://github.com/user-attachments/assets/8b655586-eee0-4728-8362-9f9e60c32d41" />


---

Mascotas

<img width="1905" height="909" alt="image" src="https://github.com/user-attachments/assets/1f2a3099-d8b7-435b-add7-92d8c8beeb3f" />


---

Servicios

<img width="1908" height="910" alt="image" src="https://github.com/user-attachments/assets/0b93a66c-11e0-4013-8e45-54d468310bc5" />


---

Reservas

<img width="1904" height="909" alt="image" src="https://github.com/user-attachments/assets/6770bbb1-3fe0-4ac9-a4c5-090bf6568063" />


---

## 📂 Estructura del proyecto

```
petlucones/
│
├── clientes/
├── mascotas/
├── reservas/
├── servicios/
├── core/
├── config/
├── static/
├── templates/
│
├── manage.py
├── requirements.txt
└── README.md
```

---

Instalación

Clonar el repositorio

```bash
git clone https://github.com/MorteAeterna/PetLucones.git
```

Entrar al proyecto

```bash
cd PetLucones
```

Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Ejecutar migraciones

```bash
python manage.py migrate
```

Crear datos de demostración

```bash
python manage.py createdemo
```

Iniciar servidor

```bash
python manage.py runserver
```

---

Funcionalidades principales

Dashboard

- Estadísticas generales
- Últimas reservas
- Próximas reservas

Clientes

- Crear
- Editar
- Eliminar
- Buscar

Mascotas

- Asociación con clientes
- Historial de reservas

Servicios

- Duración
- Precio
- Estado activo

Reservas

- Agenda visual
- Bloques horarios
- Estados
- Validaciones de disponibilidad

Autor

**Joaquín Mella**

GitHub

https://github.com/MorteAeterna

---

Licencia

Este proyecto está bajo la licencia MIT.
