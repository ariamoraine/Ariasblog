from django.conf.urls import patterns, include, url
from ariablog.views import index, signup, newuser, mylogin, mylogout, postpage, newpost, editpost, deletepost, areyousure
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	('^$', index),
	('^post/(\d{1,3})/$', postpage),
	('^post/$', newpost),
	(r'^edit/(?P<id>\d+)', editpost),
	(r'^delete/(?P<id>\d+)', deletepost),
	(r'^sure/(?P<id>\d+)', areyousure),
	('^signup/$', signup),
	('^newuser/', newuser),
	(r'^login/$', mylogin),
	(r'^logout/$', mylogout),

	# Examples:
	# url(r'^$', 'ariablog.views.home', name='home'),
	# url(r'^ariablog/', include('ariablog.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),
)
