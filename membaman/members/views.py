from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView

from django.core.urlresolvers import reverse
from .models import Family, Caregiver, Member, Person 

TEMP_ORG_NAME = 'Conversion Group'
TEMP_ORG_ID = 45 

class MemberListView(ListView):
    model = Member
    template_name = 'fees/member_list.html'
    context_object_name = "member_list"
    paginate_by = 20

#    def get_queryset(self):
#        '''
#        Provide sortation to the QS and add some extra columns
#        to contain css class names to allow the template to
#        output background colours which enhance the meaning of 
#        the data
#        '''
#
#        year_id = self.__default_yearid()
#
#        current_subyear_class = 0 
#        current_member_class = 0    
#        SUBYEAR_CSS_CLASSES = ['syon', 'syoff']
#        MEMBER_CSS_CLASSES = ['memon', 'memoff']
#
#        desc_order = False
#        qs_member = Member.objects.filter().order_by('name_family', 'name_given')
#        
#        if desc_order:
#            qs_member = qs_member.reverse()
#
#        #Setup some flags to drive colour banding in template
#        if qs_member:
#            current_familyid = qs_member[0].family.id
#            for mbr in qs_member:
#                if mbr.subyear.id != current_subyearid:
#                    current_familyid = mbr.subyear.id
#                    current_family_class = 0 if current_family_class else 1
#
#                mbr.familycssclass = SUBYEAR_CSS_CLASSES[current_family_class]
#
#            
#        return qs_member
#
