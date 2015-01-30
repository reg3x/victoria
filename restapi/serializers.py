from rest_framework import serializers
from models import Panty


class PantySerializer(serializers.ModelSerializer):
    class Meta:
        model = Panty
        fields = ('product_id', 'name', 'price', 'stock', 'description', 'img')