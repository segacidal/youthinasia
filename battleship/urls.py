from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'battleship.views.home', name='home'),
)
