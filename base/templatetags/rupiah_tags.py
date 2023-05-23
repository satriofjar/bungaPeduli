from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter
def rupiah_format(value):
    value = intcomma(value)
    return f"Rp {value}"