from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',

    url(
        r'^results/$', 
        TemplateView.as_view(template_name="googlesearch/results.html"),
        name='googlesearch-results'
    ),

    url(
        r'^cref-cse\.xml/$', 
        'googlesearch.views.cref_cse', 
        {},
        name='googlesearch-cref-cse'
    ),
)
