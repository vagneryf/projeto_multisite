from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'projeto_multisite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^admin/filebrowser/', include(site.urls)),
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    # (r'^admin/',  include(admin.site.urls)), # admin site
    (r'^tinymce/', include('tinymce.urls')),
)
