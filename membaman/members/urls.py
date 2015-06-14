from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from . import views

'''
urlpatterns = patterns('',
    url(r'^$', views.IncomeListView.as_view(), name='income-list'),
)
'''
urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='members/members-index.html'), name='membersindex'),
    url(r'^member-list/', views.MemberActiveListView.as_view(), name='member-list'),
    url(r'^member-nomore-list/', views.MemberNotActiveListView.as_view(), name='member-nomore-list'),
    url(r'^member-view/(?P<pk>\d+)/$', views.MemberDetail.as_view(), name='member-view'),
    url(r'^member-family-finance-list/', views.FamilyFinanceListView.as_view(), name='member-family-finance-list'),
    url(r'^member-finance-list/', views.MemberFinanceListView.as_view(), name='member-finance-list'),
    url(r'^family-view/(?P<pk>\d+)/$', views.FamilyDetail.as_view(), name='family-view'),
)
