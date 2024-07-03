# templatetags/cart_extras.py

from django import template

register = template.Library()

# Definición de un filtro para multiplicar
@register.filter
def multiply(value, arg):
    try:
        return value * arg
    except (ValueError, TypeError):
        return ''

@register.filter
def resta(value, arg):
    try:
        return value - arg
    except (ValueError, TypeError):
        return ''

@register.filter
def suma(value, arg):
    try:
        return value + arg
    except (ValueError, TypeError):
        return ''
