from django.conf.urls import patterns, include, url
from django.conf import  settings
from django.views.generic import RedirectView


urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT}),
    ("^", include("formexample.urls")),
    (r'^.*$', RedirectView.as_view(url='/model_form_v3/')),
)
