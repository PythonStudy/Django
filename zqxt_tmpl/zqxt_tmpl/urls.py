from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'zqxt_tmpl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$','learn.views.home',name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
