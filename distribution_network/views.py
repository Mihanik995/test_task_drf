from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from distribution_network.models import DistributionNod, Product
from distribution_network.permissions import IsActive
from distribution_network.serializers import DistribNodSerializer, ProductSerializer


class DistribNodViewSet(viewsets.ModelViewSet):
    queryset = DistributionNod.objects.all()
    serializer_class = DistribNodSerializer
    permission_classes = [IsAuthenticated, IsActive]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsActive]
