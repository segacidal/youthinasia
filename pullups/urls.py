__author__ = 'clint'
from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',

    url(r'^$', home, name='home'),
    url(r'^view_history/$', view_history, name='view_history'),
    url(r'^graph/$', graph, name='graph'),
    url(r'^to_do/$', to_do, name='to_do'),
    )