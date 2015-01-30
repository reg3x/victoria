from django.conf.urls import patterns, include, url
from restapi.views import PantyList, PantyDetail, LeggingList,\
    LeggingDetail, BrasierList, BrasierDetail, CreamList, CreamDetail,\
    ButterList, ButterDetail, FraganceList, FraganceDetail


panty_urls = patterns('',
    url(r'^$', PantyList.as_view(), name='panty-list'),
    url(r'^/(?P<pk>\d+)$', PantyDetail.as_view(), name='panty-detail')
)

legging_urls = patterns('',
    url(r'^$', LeggingList.as_view(), name='legging-list'),
    url(r'^/(?P<pk>\d+)$', LeggingDetail.as_view(), name='legging-detail')
)

brasier_urls = patterns('',
    url(r'^$', BrasierList.as_view(), name='bra-list'),
    url(r'^/(?P<pk>\d+)$', BrasierDetail.as_view(), name='bra-detail')
)

cream_urls = patterns('',
    url(r'^$', CreamList.as_view(), name='cream-list'),
    url(r'^/(?P<pk>\d+)$', CreamDetail.as_view(), name='cream-detail')
)

butter_urls = patterns('',
    url(r'^$', ButterList.as_view(), name='butter-list'),
    url(r'^/(?P<pk>\d+)$', ButterDetail.as_view(), name='butter-detail')
)

fragance_urls = patterns('',
    url(r'^$', FraganceList.as_view(), name='fragance-list'),
    url(r'^/(?P<pk>\d+)$', FraganceDetail.as_view(), name='fragance-detail')
)


catalog_urls = patterns('',
    url(r'panty', include(panty_urls)),
    url(r'legging', include(legging_urls)),
    url(r'brasier', include(brasier_urls)),
    url(r'cream', include(cream_urls)),
    url(r'butter', include(butter_urls)),
    url(r'fragance', include(fragance_urls)),
)

urlpatterns = patterns('',
    url(r'^catalog', include(catalog_urls))
)


