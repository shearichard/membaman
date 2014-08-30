from django.contrib import admin

# Register your models here.
from fees.models import Year
from fees.models import SubYear 
from fees.models import Income

admin.site.register(Year)
admin.site.register(SubYear)
admin.site.register(Income)
