from rest_framework import serializers
from order.models import *


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = "__all__"


class SalesPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesPeople
        fields = "__all__"


class PcsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pcs
        fields = "__all__"
