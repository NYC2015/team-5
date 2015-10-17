from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jpmcfg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^FeedTheChildren/', include('FeedTheChildren.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
