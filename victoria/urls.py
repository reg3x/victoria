from django.conf.urls import include, url
from rest_framework import routers
from restapi.views import PantyViewSet, LeggingViewSet, BrasierViewSet,  \
    CreamViewSet, ButterViewSet, FraganceViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'panty', PantyViewSet)
router.register(r'legging', LeggingViewSet)
router.register(r'brasier', BrasierViewSet)
router.register(r'cream', CreamViewSet)
router.register(r'butter', ButterViewSet)
router.register(r'fragance', FraganceViewSet)

urlpatterns = [
    url(r'^api/catalog/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
