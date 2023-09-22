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


class CasesViewSet(viewsets.ModelViewSet):
    queryset = Cases.objects.all()
    serializer_class = CasesSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class SignupViewSet(viewsets.ModelViewSet):
    queryset = SalesPeople.objects.all()
    serializer_class = SalesPeopleSerializer


class LoginoutViewSet(viewsets.ModelViewSet):
    queryset = SalesPeople.objects.all()
    serializer_class = LoginoutSerializer

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        responses={200: TokenSerializer()}
    )
    def login(self, request):
        account = request.data.get("account")
        password = request.data.get("password")
        password = hashlib.md5(password.encode()).hexdigest()
        salepeople = SalesPeople.objects.filter(account=account).first()
        if salepeople and salepeople.password == password:
            token, created = Token.objects.get_or_create(user=salepeople)
            return Response({"token": token.token}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )

    """
    @action(detail=False, methods=["post"])
    def logout(self, request):
        salepeople = request.user
        if salepeople.is_authenticated:
            salepeople.auth_token.delete()
            return Response({"message": "Logged out"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Not logged in"}, status=status.HTTP_401_UNAUTHORIZED
            )
    """


class PcsViewSet(viewsets.ModelViewSet):
    queryset = Pcs.objects.all()
    serializer_class = PcsSerializer
