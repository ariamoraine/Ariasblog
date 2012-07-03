from django.conf.urls import patterns, include, url
from ariablog.views import index, signup, login_view, logout_view, newuser, postpage, newpost, editpost, deletepost, areyousure
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
	(r'^login/$', login_view),
	(r'^logout/$', logout_view),
	(r'^admin/', include(admin.site.urls)),
)
