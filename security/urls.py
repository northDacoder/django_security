from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'security.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^userform/$', 'security.views.UserForm', name='userform'),
    url(r'^signupform/$', 'security.views.SignupForm', name='signupform'),
)
