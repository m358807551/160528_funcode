from django.conf.urls import patterns, include, url
from django.contrib import admin
from app_django import views as app_django_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'funcode.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', app_django_views.index),
    url(r'^judge/', app_django_views.judge),
)