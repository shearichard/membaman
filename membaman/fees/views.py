from django.shortcuts import render

from django.views.generic import ListView, DetailView, UpdateView

from django.core.urlresolvers import reverse

from .models import Year, SubYear, Income

class IncomeListView(ListView):
    model = Income
    template_name = 'fees/income_list_simple.html'
    context_object_name = "income_list"
    paginate_by = 10

    def get_queryset(self):
        '''
        Provide sortation to the QS and add some extra columns
        to contain css class names to allow the template to
        output background colours which enhance the meaning of 
        the data
        '''
        current_subyear_class = 0 
        current_member_class = 0    
        SUBYEAR_CSS_CLASSES = ['syon', 'syoff']
        MEMBER_CSS_CLASSES = ['memon', 'memoff']

        desc_order = False
        qs_income = super(IncomeListView, self).get_queryset().order_by('member__name_family', 'member__name_given', 'subyear__start', 'subyear__end')
        if desc_order:
            qs_income = qs_income.reverse()

        #Setup some flags to drive colour banding in template
        current_subyearid = qs_income[0].subyear.id
        current_memberid = qs_income[0].member.id
        for inc in qs_income:
            if inc.subyear.id != current_subyearid:
                current_subyearid = inc.subyear.id
                current_subyear_class = 0 if current_subyear_class else 1
            if inc.member.id != current_memberid:
                current_memberid = inc.member.id
                current_member_class = 0 if current_member_class else 1

            inc.subyearcssclass = SUBYEAR_CSS_CLASSES[current_subyear_class]
            inc.membercssclass = MEMBER_CSS_CLASSES[current_member_class]

            
        return qs_income
