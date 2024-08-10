from rest_framework import routers

from distribution_network.views import DistribNodViewSet, ProductViewSet

nods_router = routers.DefaultRouter()
nods_router.register(r'distrib_nods', DistribNodViewSet)

products_router = routers.DefaultRouter()
products_router.register(r'products', ProductViewSet)

urlpatterns = [] + nods_router.urls + products_router.urls
