from django.conf.urls import patterns, include, url
from ariablog.views import index, postpage, newpost

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	('^$', index),
	('^post/(\d{1,3})/$', postpage),
	('^post/$', newpost),

    # Examples:
    # url(r'^$', 'ariablog.views.home', name='home'),
    # url(r'^ariablog/', include('ariablog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
