from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView
admin.site.site_header = 'MembaMan Administration Area'
admin.site.site_title = 'MembaMan Admin'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'membaman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', RedirectView.as_view(url='/fees/')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fees/', include('fees.urls', namespace="fees")),
    url(r'^members/', include('members.urls', namespace="members")),
    url(r'^membaman/', include('membaman.urls', namespace="membaman")),
    url(r'^feedback', include('feedback.urls')),
)
