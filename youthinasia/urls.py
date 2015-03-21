from django.conf.urls import patterns, include, url
from youthinasia.views import hello, current_datetime, hours_ahead, form_page, display_meta, thanks
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Admin and testing
    url(r'^$', hello),
    (r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello, name='hello'),
    url(r'^time/$', current_datetime, name='time'),
    url(r'^time/plus/(\d{1,2})$', hours_ahead),
    url(r'^form/$', form_page, name='form'),
    url(r'^thanks/$', thanks),
    url(r'^meta/$', display_meta, name='meta'),


    # Other apps
    url(r'^gallery/',include('gallery.urls', namespace='gallery')),
    url(r'^battleship/$', include('battleship.urls', namespace='battleship')),
    url(r'^pullups/', include('pullups.urls', namespace='pullups')),
    url(r'^gymlog/', include('gymlog.urls', namespace='gymlog')),
) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)