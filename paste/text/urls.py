from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns("text.views",
    url(r'^new/', 'new'),
    url(r'^create/', 'create'),
    url(r'^show/(?P<paste_id>\d+)/', 'show'),
)
