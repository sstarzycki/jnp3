from django.conf.urls.defaults import patterns, include, url

from text.api import ListTexts, ShowText
from djangorestframework.views import ListOrCreateModelView, InstanceModelView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'paste.text.views.show_main', name='home'),
    url(r'^openid/', include('paste.django_openid_auth.urls')),
    url(r'^paste/', include('paste.text.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.static',
            (r'^media/(?P<path>.*)$',
                'serve',
                { 'document_root': 'media/',
                 'show_indexes': True }),)


urlpatterns += patterns("api",
    url(r'^api/$', ListTexts.as_view()),
    url(r'^api/(?P<key>[A-Za-z0-9]*$)', ShowText.as_view()),
)
