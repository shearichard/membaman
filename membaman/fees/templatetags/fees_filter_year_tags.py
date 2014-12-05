from ..models import Year, SubYear, Income
from ..views import TEMP_ORG_ID

from django import template
from django.template.loader import get_template

register = template.Library()
@register.assignment_tag
def income_year_select_content():
    year_list = Year.objects.filter(organisation_id=TEMP_ORG_ID).distinct('start')
    return year_list
