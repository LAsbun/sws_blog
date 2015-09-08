from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'swsblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),

    url(r'^archieve/$', views.archieve, name='archieve'),
    url(r'^aboutme/$', views.aboutme, name='aboutme'),
    url(r'^search(?P<tag>\w*)/$', views.search_tag, name = 'search_tag')
    #url(r'^/(?P<id>\d+)/$', views.detail, name='detail'),
]
