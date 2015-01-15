from django.conf.urls import patterns, include, url
from django.contrib import admin
from restapi.views import ProductList, ProductDetail

product_urls = patterns('',
    url(r'^$', ProductList.as_view(), name='product-list'),
    url(r'^/(?P<pk>\d+)$', ProductDetail.as_view(), name='product-detail')
)

urlpatterns = patterns('',
    url(r'^products', include(product_urls))
)
