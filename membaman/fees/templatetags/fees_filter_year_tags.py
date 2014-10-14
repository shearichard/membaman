from ..models import Year, SubYear, Income

from django import template
from django.template.loader import get_template

register = template.Library()
#---g = get_template('fees/income_list_simple.html')
#---@register.inclusion_tag("fees/income_list_simple.html")
#---def income_year_select():
#---    #year_list = Year.objects.order_by('start', 'end').distinct('start')
#---    year_list = Year.objects.all()
#---    #import pdb; pdb.set_trace()
#---    #year_list = [] 
#---    #year_list.append({'id':'1', 'name':'1irst'})
#---    #year_list.append({'id':'2', 'name':'2irst'})
#---    #year_list.append({'id':'3', 'name':'3irst'})
#---    return {'year_list' : year_list}
#---
#---#@register.inclusion_tag("fees/income_list_simple.html")
#---#register.inclusion_tag("fees/income_list_simple.html")(income_year_select)
#---from django.template.loader import get_template
#---def show_results():
#---    choices = "This is a string" 
#---    return {'choices': choices}
#---
#---gg = get_template('fees/income_list_simple.html')
#---register.inclusion_tag(gg)(show_results)
#---
@register.assignment_tag
def get_activities_it_works():
#    return ("A", "B")
     year_list = [] 
     year_list.append({'id':'1', 'name':'1irst'})
     year_list.append({'id':'2', 'name':'2irst'})
     year_list.append({'id':'3', 'name':'3irst'})
     return {'year_list' : year_list}
@register.assignment_tag
def get_activities_this_works_too():
    year_list = Year.objects.all()
    return {'year_list' : year_list}
@register.assignment_tag
def income_year_select_content():
    year_list = Year.objects.all().distinct('start')
    return year_list
