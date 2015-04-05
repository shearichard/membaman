import datetime

from django.shortcuts import render

from django.views.generic import ListView, DetailView, UpdateView

from django.core.urlresolvers import reverse

from .models import Year, SubYear, Income
from members.models import Member

#TEMP_ORG_NAME = 'Conversion Group'
TEMP_ORG_ID = 71 
TEMP_CURR_YR_START = datetime.date(2015,1,1)
TEMP_CURR_YR_FINISH = datetime.date(2015,12,31)

class IncomeListView(ListView):
    model = Income
    template_name = 'fees/income_list_simple.html'
    context_object_name = "income_list"
    paginate_by = 15

    def __default_yearid(self):
        year_id = self.request.GET.get('year', None)
        if not year_id:
            try:
                obj_year = Year.objects.get(organisation_id=TEMP_ORG_ID, start__lte=datetime.datetime.now(), end__gte=datetime.datetime.now())
            except Year.DoesNotExist:
                lst_year = Year.objects.filter(organisation_id=TEMP_ORG_ID).order_by('start')
                if lst_year:
                    obj_year = lst_year[0]
                else:
                    #If this happens something else is broken
                    raise
            year_id = obj_year.id

        return year_id


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IncomeListView, self).get_context_data(**kwargs)
        # Add in a the year that's just been selected to allow us to 
        # to select the correct element of the  the dropdown.
        year_id = self.__default_yearid()
        context['year_id'] = int(year_id)
        return context

    def get_queryset(self):
        '''
        Provide sortation to the QS and add some extra columns
        to contain css class names to allow the template to
        output background colours which enhance the meaning of 
        the data
        '''

        year_id = self.__default_yearid()

        current_subyear_class = 0 
        current_member_class = 0    
        SUBYEAR_CSS_CLASSES = ['syon', 'syoff']
        MEMBER_CSS_CLASSES = ['memon', 'memoff']

        desc_order = False
        qs_income = Income.objects.filter(subyear__year_id=year_id).order_by('member__name_family', 'member__name_given', 'subyear__start', 'subyear__end')
        
        if desc_order:
            qs_income = qs_income.reverse()

        #Setup some flags to drive colour banding in template
        if qs_income:
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

class IncomeListSubYearView(ListView):
    model = Income
    template_name = 'fees/income_list_by_subyear.html'
    context_object_name = "income_list"
    paginate_by = 10

    def get_queryset(self):
        dic_out = {}
        suby_order_list = []
        mem_order_list = []

        qs_subyear = SubYear.objects.filter(year__organisation__pk=TEMP_ORG_ID, start__gte=TEMP_CURR_YR_START, end__lte=TEMP_CURR_YR_FINISH).order_by('start')
        qs_mem = Member.objects.filter(organisation__pk=TEMP_ORG_ID).order_by( 'name_family', 'family__id','name_given')
        import pdb; pdb.set_trace()

        for suby in qs_subyear:
            if suby.name not in dic_out:
                dic_out[suby.name] = {}
                suby_order_list.append(suby.name)
            for mem in qs_mem:
                if mem.id not in dic_out[suby.name]:
                    dic_out[suby.name][mem.id] = {}
                    mem_order_list.append(mem.id)

                qs_income = Income.objects.filter(subyear=suby, member=mem).order_by('subyear__start')

                for inc in qs_income:
                    dic_out[suby.name][mem.id] = inc.received 


        return qs_income
