#coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^accounts/register/$',"jeap.views.register"),
    url(r"^accounts/login/$","django.contrib.auth.views.login",{'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^base1/$','jeap.views.base1'),
    #url(r'^a/$','jeap.views.a'),
    url(r'^add/$','jeap.views.add'),
    url(r'^test/(\d{1,2})/$','jeap.views.test'),
)
