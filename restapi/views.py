from rest_framework import viewsets
from serializers import PantySerializer, LeggingSerializer, BrasierSerializer, CreamSerializer,\
    ButterSerializer, FraganceSerializer
from models import Panty, Legging, Brasier, Cream, Butter, Fragance


class PantyViewSet(viewsets.ModelViewSet):
    queryset = Panty.objects.all()
    serializer_class = PantySerializer


class LeggingViewSet(viewsets.ModelViewSet):
    queryset = Legging.objects.all()
    serializer_class = LeggingSerializer


class BrasierViewSet(viewsets.ModelViewSet):
    queryset = Brasier.objects.all()
    serializer_class = BrasierSerializer


class CreamViewSet(viewsets.ModelViewSet):
    queryset = Cream.objects.all()
    serializer_class = CreamSerializer


class ButterViewSet(viewsets.ModelViewSet):
    queryset = Butter.objects.all()
    serializer_class = ButterSerializer


class FraganceViewSet(viewsets.ModelViewSet):
    queryset = Fragance.objects.all()
    serializer_class = FraganceSerializer