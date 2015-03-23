from django.contrib import admin

# Register your models here.
from members.models import Organisation
from members.models import SubOrganisation
from members.models import Family
from members.models import Caregiver
from members.models import Member
from members.admin_action import print_start_year_invoices

class FamilyAdmin(admin.ModelAdmin):
        list_display = ['street_address', 'suburb', 'city', 'phone_fixed']
        list_filter = ['suburb']

class SubOrganisationAdmin(admin.ModelAdmin):
        list_display = ['sub_name', 'organisation_name']
        list_filter = ['organisation']
class CaregiverAdmin(admin.ModelAdmin):
        list_display = ['name_given', 'name_family', 'email',  'relationship']
        search_fields = ['name_given', 'name_family']
class MemberAdmin(admin.ModelAdmin):
        list_display = ['name_family', 'name_given', 'organisation', 'sub_organisation', 'membership_type', 'no_longer_attends']
        list_filter = ['organisation', 'sub_organisation', 'family']
        search_fields = ['name_given', 'name_family']
        actions = [print_start_year_invoices] 

admin.site.register(Organisation)
admin.site.register(SubOrganisation, SubOrganisationAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(Caregiver, CaregiverAdmin)
admin.site.register(Member, MemberAdmin)
