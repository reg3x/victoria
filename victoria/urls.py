from django.conf.urls import patterns, include, url
from django.contrib import admin
from restapi.views import PantyList, PantyDetail

panty_urls = patterns('',
    url(r'^$', PantyList.as_view(), name='panty-list'),
    url(r'^/(?P<pk>\d+)$', PantyDetail.as_view(), name='panty-detail')
)

urlpatterns = patterns('',
    url(r'^panty', include(panty_urls))
)
