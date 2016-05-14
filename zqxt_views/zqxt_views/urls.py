from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'zqxt_views.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^add/(\d+)/(\d+)/$','calc.views.add',name='add'),
    url(r'^admin/', include(admin.site.urls)),
)
