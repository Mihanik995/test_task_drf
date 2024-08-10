from rest_framework import serializers

from distribution_network.models import Product, DistributionNod
from distribution_network.validators import ProviderValidator


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'model', 'release_date')


class DistribNodSerializer(serializers.ModelSerializer):
    dept = serializers.FloatField(read_only=True)
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = DistributionNod
        fields = ('title', 'role', 'email', 'country', 'city', 'street', 'building',
                  'products', 'provider', 'dept', 'creation_datetime')
        validators = [ProviderValidator()]
