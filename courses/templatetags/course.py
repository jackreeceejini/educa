from ast import expr_context
from inspect import Attribute
from django import template 

register = template.Library()

@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name 
    except AttributeError:
        return None 

        