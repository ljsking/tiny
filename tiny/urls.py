from django.conf.urls.defaults import patterns, include, url

from posts.views import index, done, logout, error

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tiny.views.home', name='home'),
    url(r'^$', index, name='index'),
    url(r'^posts/$', 'posts.views.index'),
    url(r'^posts/post/$', 'posts.views.post'),
    url(r'^done/$', done, name='done'),
    url(r'^error/$', error, name='error'),
    url(r'^logout/$', logout, name='logout'),
    url(r'', include('social_auth.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
