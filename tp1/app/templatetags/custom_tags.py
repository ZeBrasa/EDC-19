from django import template
from django.conf import settings
import lxml

register = template.Library()


@register.filter
def get_attr(elem, attr):
    return elem.get(attr)
