# Create your views here.
from order.models import *
from order.serializers import *
from rest_framework import viewsets


# Create your views here.
class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class CasesViewSet(viewsets.ModelViewSet):
    queryset = Cases.objects.all()
    serializer_class = CasesSerializer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class SalePeopleViewSet(viewsets.ModelViewSet):
    queryset = SalesPeople.objects.all()
    serializer_class = SalesPeopleSerializer


class PcsViewSet(viewsets.ModelViewSet):
    queryset = Pcs.objects.all()
    serializer_class = PcsSerializer
