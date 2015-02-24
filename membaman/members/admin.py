from django.contrib import admin

# Register your models here.
from members.models import Organisation
from members.models import SubOrganisation
from members.models import Family
from members.models import Caregiver
from members.models import Member

class FamilyAdmin(admin.ModelAdmin):
        list_display = ['street_address', 'suburb', 'city', 'phone_fixed']
        list_filter = ['suburb']

class SubOrganisationAdmin(admin.ModelAdmin):
        list_display = ['sub_name', 'organisation_name']
        list_filter = ['organisation']
class CaregiverAdmin(admin.ModelAdmin):
        list_display = ['name_given', 'name_family', 'relationship']
class MemberAdmin(admin.ModelAdmin):
        list_display = ['name_family', 'name_given', 'organisation', 'sub_organisation', 'membership_type']
        list_filter = ['organisation', 'sub_organisation', 'family']

admin.site.register(Organisation)
admin.site.register(SubOrganisation, SubOrganisationAdmin)
admin.site.register(Family, FamilyAdmin)
admin.site.register(Caregiver, CaregiverAdmin)
admin.site.register(Member, MemberAdmin)
