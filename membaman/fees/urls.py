from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from . import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='fees/fees-index.html'), name='feesindex'),
    url(r'^income-list/', views.IncomeListView.as_view(), name='income-list'),
    url(r'^income-list-subyear/', views.IncomeListSubYearView.as_view(), name='income-list-subyear'),
)
