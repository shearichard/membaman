from ..models import Year, SubYear, Income

from django import template
from django.template.loader import get_template

register = template.Library()
@register.assignment_tag
def income_year_select_content():
    year_list = Year.objects.all().distinct('start')
    return year_list
