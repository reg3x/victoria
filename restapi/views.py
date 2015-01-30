from django.shortcuts import render
from rest_framework import generics, permissions

from serializers import PantySerializer
from models import Panty

class PantyList(generics.ListCreateAPIView):
    queryset = Panty.objects.all()
    serializer_class = PantySerializer
    permission_classes = [permissions.AllowAny]


class PantyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Panty.objects.all()
    serializer_class = PantySerializer
    permission_classes = [permissions.AllowAny]

