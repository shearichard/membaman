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
    url(r'^member-list/', views.MemberListView.as_view(), name='member-list'),
    url(r'^member-nomore-list/', views.MemberNoMoreListView.as_view(), name='member-nomore-list'),
)
