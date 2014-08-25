from django.contrib import admin

# Register your models here.
from members.models import Organisation
from members.models import SubOrganisation
from members.models import Family
from members.models import Caregiver
from members.models import Member

admin.site.register(Organisation)
admin.site.register(SubOrganisation)
admin.site.register(Family)
admin.site.register(Caregiver)
admin.site.register(Member)
