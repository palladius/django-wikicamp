from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wikicamp.views.home', name='home'),
    # url(r'^wikicamp/', include('wikicamp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # For wiki
    url(r'^wikicamp/(?P<page_name>[^/]+)/edit/$', 'wiki.views.edit_page'),
    url(r'^wikicamp/(?P<page_name>[^/]+)/save/$', 'wiki.views.save_page'),
    url(r'^wikicamp/(?P<page_name>[^/]+)/$',      'wiki.views.view_page'),

)
