          # -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('smartfreeze.catalog.urls')),
    (r'^cart/', include('smartfreeze.cart.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^myadmin/', include('smartfreeze.myadmin.urls')),
    (r'^tinymce/', include('tinymce.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns ('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': settings.MEDIA_ROOT}),
    )
urlpatterns += staticfiles_urlpatterns()
