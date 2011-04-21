          # -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('smartfreeze.catalog.urls')),
    (r'^cart/', include('smartfreeze.cart.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns ('',
          # Статика для тестового веб сервера
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': settings.MEDIA_ROOT}),
    )