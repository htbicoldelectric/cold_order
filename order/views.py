# Create your views here.
from order.models import Orders, Clients, SalesPeople
from order.serializers import OrdersSerializer, ClientsSerializer, SalesPeopleSerializer
from rest_framework import viewsets


# Create your views here.
class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class SalePeopleViewSet(viewsets.ModelViewSet):
    queryset = SalesPeople.objects.all()
    serializer_class = SalesPeopleSerializer
