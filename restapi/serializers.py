from rest_framework import serializers
from models import Panty, Legging, Brasier, Cream, Butter, Fragance


class PantySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Panty
        fields = ('product_id', 'name', 'price', 'stock', 'description', 'img')


class LeggingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Legging
        fields = ('product_id', 'name', 'price', 'stock', 'description', 'img')


class BrasierSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brasier
        fields = ('product_id', 'name', 'price', 'stock', 'description', 'img')


class CreamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cream
        fields = ('product_id', 'name', 'price', 'stock', 'description', 'img')


class ButterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Butter
        fields = ('product_id', 'name', 'price', 'stock', 'description', 'img')


class FraganceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fragance
        fields = ('product_id', 'name', 'price', 'stock', 'description', 'img')
