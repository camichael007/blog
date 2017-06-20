from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/index/$', 'blog.views.index'),
    url(r'^blog/time/$', 'blog.views.current_datetime'),
    url(r'^time/plus/(\d{1,2})/$', 'blog.views.hours_ahead'),
    url(r'^blog/thanks/$', 'blog.views.mail_thank'),
                       
)
