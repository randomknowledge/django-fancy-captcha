# coding=utf-8
from django.conf.urls import patterns, url
from django_fancy_captcha import views


urlpatterns = patterns(
    '',
    url(r'(?P<cube_num>\d)/(?P<image_num>\d)/(?P<num_cubes>\d)\.jpg$', views.image, name='image'),
)
