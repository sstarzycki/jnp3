from django.conf.urls.defaults import patterns, include, url
from text.views import NewTextView, ListTextView, ShowTextView

urlpatterns = patterns("text.views",
    (r'^new/$', NewTextView.as_view()),
    (r'^list/$', ListTextView.as_view()),
    (r'^show/(?P<pk>[a-z0-9]+)/$', ShowTextView.as_view()),
)
