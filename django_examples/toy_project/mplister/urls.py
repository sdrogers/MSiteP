from django.conf.urls import patterns, url

from mplister import views

urlpatterns = patterns('',
	url(r'^$',views.index,name='index'),
	url(r'^party/(?P<party_name>\w+)/$', views.party, name = 'party'),
	url(r'^msp/(?P<msp_name_url>\w+)/$', views.msp, name = 'msp'),
	url(r'^random/',views.random,name='random'),)