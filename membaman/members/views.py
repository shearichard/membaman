from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView

from django.core.urlresolvers import reverse
from django.db.models import Count
from .models import Family, Caregiver, Member, Person 

TEMP_ORG_NAME = 'Conversion Group'
TEMP_ORG_ID = 45 

class MemberDetail(DetailView):
    model = Member
    context_object_name = "member_detail"

class MemberListView(ListView):
    model = Member
    template_name = 'members/member_list.html'
    context_object_name = "member_list"
    paginate_by = 100

    def get_queryset(self, active):
        mem = Member.objects.filter(no_longer_attends=active)
        return mem


class MemberActiveListView(MemberListView):
    def get_queryset(self):
        return super(MemberActiveListView, self).get_queryset(active=False)


class MemberNotActiveListView(MemberListView):
    def get_queryset(self):
        return super(MemberNotActiveListView, self).get_queryset(active=True)

class FamilyListView(ListView):
    model = Family 
    template_name = 'members/family_list.html'
    context_object_name = "family_list"
    paginate_by = 100

    def get_queryset(self):
        fam = Family.objects.all()
        return fam

class FamilyFinanceListView(FamilyListView):

    def get_queryset(self):
        fam = Family.objects.all().annotate(count_members=Count('member'))
        #return super(FamilyFinanceListView, self)
        return fam

class FamilyDetail(DetailView):
    model = Family
    context_object_name = "family_detail"

