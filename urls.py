# coding=utf-8
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(
        r'^admin/',
        include(admin.site.urls)
    ),

    url(
        r'captcha/',
        include('django_fancy_captcha.urls')
    ),

    url(
        r'',
        include('example.urls')
    ),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    )
