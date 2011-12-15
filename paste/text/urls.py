from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns("text.views",
    url(r'^new/', 'new'),
)
