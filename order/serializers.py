from rest_framework import serializers
from order.models import *
import hashlib

class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ["token"]
        


class ClientsSerializer(serializers.ModelSerializer):
    #token = TokenSerializer()

    class Meta:
        model = Clients
        fields = "__all__"


class SalePeopleSerializer(serializers.ModelSerializer):
    #token = TokenSerializer()

    class Meta:
        model = SalesPeople
        fields = "__all__"


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesPeople
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop("password")
        encrypt_password = hashlib.md5(password.encode()).hexdigest()
        d = validated_data
        d.update(dict(password=encrypt_password))
        user = SalesPeople.objects.create(**d)
        return user


class LoginTokenSerializer(serializers.ModelSerializer):
    success = serializers.BooleanField()

    class Meta:
        model = Token
        fields = ["token", "success"]
        extra_kwargs = {
            "success": {"read_only": True},
        }


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesPeople
        fields = ["account", "password"]
        extra_kwargs = {
            "account": {"write_only": True},
            "password": {"write_only": True},
        }


class LogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ["token", "success"]
        extra_kwargs = {
            "token": {"write_only": True},
            "success": {"read_only": True},
        }


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
    token = LoginTokenSerializer()

    class Meta:
        model = Orders
        fields = "__all__"
