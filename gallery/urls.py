from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'gallery.views.home', name='home'),
    url(r'^addgallery/$', 'gallery.views.addgallery', name='addgallery'),
    url(r'^(?P<slug>.+)/$', 'gallery.views.gallery', name='view'),
)