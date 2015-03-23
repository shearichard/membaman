from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView

from django.core.urlresolvers import reverse
from .models import Family, Caregiver, Member, Person 

TEMP_ORG_NAME = 'Conversion Group'
TEMP_ORG_ID = 45 

class MemberActiveListView(ListView):
    model = Member
    template_name = 'fees/member_list.html'
    context_object_name = "member_list"
    paginate_by = 100

    def get_queryset(self):
        mem_active = Member.objects.filter(no_longer_attends=False)
        lst_mem_active = sorted(mem_active,  key=lambda m: m.last_first_name)
        return lst_mem_active

class MemberNotActiveListView(ListView):
    model = Member
    template_name = 'fees/member_list.html'
    context_object_name = "member_list"
    paginate_by = 100

    def get_queryset(self):
        '''
        Sortation shown here derived from : http://stackoverflow.com/a/4175785/364088
        '''
        mem_not_active = Member.objects.filter(no_longer_attends=True)
        lst_mem_not_active = sorted(mem_not_active,  key=lambda m: m.last_first_name)
        return mem_not_active

