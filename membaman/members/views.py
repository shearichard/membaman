from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView

from django.core.urlresolvers import reverse
from django.db.models import Count, Sum, F
from .models import Family, Caregiver, Member, Person 

TEMP_ORG_NAME = 'Conversion Group'
TEMP_ORG_ID = 45 

class MemberDetail(DetailView):
    model = Member
    context_object_name = "member_detail"

class MemberDebtorsListView(ListView):
    model = Member
    template_name = 'members/member_debtors_list.html'
    context_object_name = "member_list"
    paginate_by = 100

    def get_queryset(self):

        #The last 'exclude' in the following filter seems to be excluding rows which
        #should not be excluded. I'm not sure what it was there for in the first place
        #or the full effect of removing it but it's certainly the case that there are
        #people who owe money who won't appear in the output if that exclude is in place
        #
        #Update: I think the problem are those people who've never paid anything . Those
        #people are excluded via that exclude and that is not a good idea.
        mem = Member.objects.filter(no_longer_attends=False)\
                            .annotate(debt_total=Sum('accountentry__accountdebt__amount'))\
                            .annotate(payment_total=Sum('accountentry__accountpayment__amount'))\
                            .annotate(debt=Sum('accountentry__accountpayment__amount'))\
                            .filter(debt_total__gt=0)\
                            .exclude(payment_total__gte=F('debt_total'))

        return mem

class MemberFinanceListView(ListView):
    model = Member
    template_name = 'members/member_finance_list.html'
    context_object_name = "member_list"
    paginate_by = 100

    def get_queryset(self):

        mem = Member.objects.filter(no_longer_attends=False).annotate(debt_total=Sum('accountentry__accountdebt__amount'), payment_total=Sum('accountentry__accountpayment__amount'))
        return mem

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

