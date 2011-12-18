from django.conf.urls.defaults import patterns, include, url
from ecomstore import settings
import os

#get the current path of the project: similar to saying "/Users/christopherfarm/Desktop/ecomstore/"
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__).decode('utf-8'))


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       
                       # Examples:
    # url(r'^$', 'ecomstore.views.home', name='home'),
    # url(r'^ecomstore/', include('ecomstore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
                           url(r'^admin/', include(admin.site.urls)),
                       (r'^', include('catalog.urls')),
                       (r'^cart/$', include('cart.urls')),
     
)



#use for the previews app
urlpatterns += patterns('', 
                        (r'^catalog/$', 'preview.views.home'),
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve', 
                         {'document_root' :os.path.join(CURRENT_PATH, 'static')}),
)
handler404 = 'ecomstore.views.file_not_found_404'
