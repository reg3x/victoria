from rest_framework import generics, permissions

from serializers import PantySerializer, LeggingSerializer, BrasierSerializer, CreamSerializer,\
    ButterSerializer, FraganceSerializer
from models import Panty, Legging, Brasier, Cream, Butter, Fragance


class PantyList(generics.ListCreateAPIView):
    queryset = Panty.objects.all()
    serializer_class = PantySerializer
    permission_classes = [permissions.AllowAny]


class PantyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Panty.objects.all()
    serializer_class = PantySerializer
    permission_classes = [permissions.AllowAny]


class LeggingList(generics.ListCreateAPIView):
    queryset = Legging.objects.all()
    serializer_class = LeggingSerializer
    permission_classes = [permissions.AllowAny]


class LeggingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Legging.objects.all()
    serializer_class = LeggingSerializer
    permission_classes = [permissions.AllowAny]


class BrasierList(generics.ListCreateAPIView):
    queryset = Brasier.objects.all()
    serializer_class = BrasierSerializer
    permission_classes = [permissions.AllowAny]


class BrasierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brasier.objects.all()
    serializer_class = BrasierSerializer
    permission_classes = [permissions.AllowAny]


class CreamList(generics.ListCreateAPIView):
    queryset = Cream.objects.all()
    serializer_class = CreamSerializer
    permission_classes = [permissions.AllowAny]


class CreamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cream.objects.all()
    serializer_class = CreamSerializer
    permission_classes = [permissions.AllowAny]


class ButterList(generics.ListCreateAPIView):
    queryset = Butter.objects.all()
    serializer_class = ButterSerializer
    permission_classes = [permissions.AllowAny]


class ButterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Butter.objects.all()
    serializer_class = ButterSerializer
    permission_classes = [permissions.AllowAny]


class FraganceList(generics.ListCreateAPIView):
    queryset = Fragance.objects.all()
    serializer_class = FraganceSerializer
    permission_classes = [permissions.AllowAny]


class FraganceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fragance.objects.all()
    serializer_class = FraganceSerializer
    permission_classes = [permissions.AllowAny]