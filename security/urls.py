from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'users.views.index', name='index'),
    url(r'^secret/$', 'securityapp.views.special_page', name='secret'),
    url(r'^accounts/', include('registration.backends.default.urls')),

    # Examples:
    # url(r'^$', 'security.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^signup/$', 'securityapp.views.signup', name='signup'),
    # url(r'^accounts/login/$', 'securityapp.views.login_page', name='login'),

)
