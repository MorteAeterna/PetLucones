from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def estado_badge(estado):
    clases = {
        "Pendiente": "badge-estado-pendiente",
        "Confirmada": "badge-estado-confirmada",
        "En Proceso": "badge-estado-proceso",
        "Finalizada": "badge-estado-finalizada",
        "Cancelada": "badge-estado-cancelada",
    }

    clase = clases.get(estado, "badge-estado-default")

    return mark_safe(
        f'<span class="badge-estado {clase}">{estado}</span>'
    )


@register.filter
def clp(valor):
    try:
        valor = int(valor)
        return f"${valor:,}".replace(",", ".")
    except (ValueError, TypeError):
        return "$0"