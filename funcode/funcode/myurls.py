from app_a12 import views as app_a12_views
from django.conf.urls import patterns, include, url
from django.contrib import admin
from app_django import views as app_django_views
from app_cplusplus import views as app_cplusplus_views
from app_rzrk import views as app_rzrk_views
from app_vs2008 import views as app_vs2008_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'funcode.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^django/index/', app_django_views.index),
    url(r'^django/judge/', app_django_views.judge),
    url(r'^cplusplus/index/', app_cplusplus_views.index),
    url(r'^cplusplus/judge/', app_cplusplus_views.judge),
    url(r'^rzrk/index/', app_rzrk_views.index),
    url(r'^rzrk/judge/', app_rzrk_views.judge),
    url(r'^vs2008/index/', app_vs2008_views.index),
    url(r'^vs2008/judge/', app_vs2008_views.judge),
    url(r'^a12/index/', app_a12_views.index),
    url(r'^a12/judge/', app_a12_views.judge),
    )