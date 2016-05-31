from django.conf.urls import patterns, include, url
from django.contrib import admin
from app_django import views as app_django_views
from app_cplusplus import views as app_cplusplus_views
from app_rzrk import views as app_rzrk_views

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
)
