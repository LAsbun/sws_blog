from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'swsblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^/?(?P<id>\d{0,3})/?$', views.si),
    url(r'^/?detail/$', views.detail),
]
