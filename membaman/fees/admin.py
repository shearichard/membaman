from django.contrib import admin

# Register your models here.
from fees.models import Year
from fees.models import SubYear
from fees.models import Income
from fees.models import AccountDebt
from fees.models import AccountPayment
from fees.models import ReferenceMapper


class YearAdmin(admin.ModelAdmin):
        list_display = ['name', 'organisation', 'start', 'end']
        list_filter = ['organisation', 'start']

class SubYearAdmin(admin.ModelAdmin):
        list_display = ['year_name', 'organisation_name', 'name', 'start', 'end']
        list_filter = ['year__name', 'year__organisation']

class IncomeAdmin(admin.ModelAdmin):
        list_display = ['year_name', 'subyear_name', 'member', 'received']
        list_filter = ['subyear__year__name', 'subyear__name']

class AccountDebtAdmin(admin.ModelAdmin):
        list_display = ['member', 'date', 'amount']
        list_filter = ['member']

class AccountPaymentAdmin(admin.ModelAdmin):
        list_display = ['member', 'date', 'amount']
        list_filter = ['member']

class ReferenceMapperAdmin(admin.ModelAdmin):
        list_filter = ['payment_reference_used','payment_reference_intended']

admin.site.register(Year, YearAdmin)
admin.site.register(SubYear, SubYearAdmin)
admin.site.register(Income, IncomeAdmin)
admin.site.register(AccountDebt, AccountDebtAdmin)
admin.site.register(AccountPayment, AccountPaymentAdmin)
admin.site.register(ReferenceMapper, ReferenceMapperAdmin)
