# Create your views here.
from order.models import *
from order.serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    http_method_names = ["get", "post"]


class CasesViewSet(viewsets.ModelViewSet):
    queryset = Cases.objects.all()
    serializer_class = CasesSerializer
    http_method_names = ["get", "post"]


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    http_method_names = ["get", "post"]


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    http_method_names = ["get", "post"]


class SignupViewSet(viewsets.ModelViewSet):
    queryset = SalesPeople.objects.all()
    serializer_class = SignupSerializer
    http_method_names = ["post"]

class SalepeopleViewSet(viewsets.ModelViewSet):
    queryset = SalesPeople.objects.all()
    serializer_class = SignupSerializer
    http_method_names = ["get"]

class LoginViewSet(viewsets.ModelViewSet):
    queryset = SalesPeople.objects.all()
    serializer_class = LoginSerializer
    http_method_names = ["post"]

    # @action(detail=False, methods=["post"])
    @swagger_auto_schema(responses={200: TokenSerializer()})
    def create(self, request):
        account = request.data.get("account")
        password = request.data.get("password")
        password = hashlib.md5(password.encode()).hexdigest()
        salepeople = SalesPeople.objects.filter(account=account).first()
        if salepeople and salepeople.password == password:
            token, created = Token.objects.get_or_create(user=salepeople)
            return Response(
                {"success": token.success, "token": token.token},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )


class LogoutViewSet(viewsets.ModelViewSet):
    queryset = Token.objects.all()
    serializer_class = LogoutSerializer
    http_method_names = ["post"]
    def create(self, request):
        token = request.data.get("token")
        token = Token.objects.filter(token=token).first()
        if token:
            token.delete()
            return Response({"success": token.success}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Not logged in"}, status=status.HTTP_401_UNAUTHORIZED
            )


class PcsViewSet(viewsets.ModelViewSet):
    queryset = Pcs.objects.all()
    serializer_class = PcsSerializer
    http_method_names = ["get", "post"]
