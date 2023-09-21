from rest_framework import serializers
from order.models import *


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


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class PcsProductOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PcsProductOrders
        fields = "__all__"


class CaseCartSerializer(serializers.ModelSerializer):
    pcs_list = PcsProductOrdersSerializer(many=True)

    class Meta:
        model = CaseCart
        fields = "__all__"


class CasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cases
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):
    product_list = CaseCartSerializer(many=True)

    class Meta:
        model = Orders
        fields = "__all__"
