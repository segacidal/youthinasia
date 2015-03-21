from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'gymlog.views.home', name='home'),
    url(r'day/(?P<slug>[-\w]+)/$', 'gymlog.views.day', name='day'),
    url(r'exercise/(?P<slug>[-\w]+)/$', 'gymlog.views.exercise', name='exercise'),

    url(r'thanks/$', 'gymlog.views.form_success', name='form_success'),

    url(r'dev/$', 'gymlog.views.dev', name='dev'),
    )