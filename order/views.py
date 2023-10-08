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
    http_method_names = ["get", "post", "options"]

    @action(detail=False, methods=["GET"])
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="case id",
                in_=openapi.IN_QUERY,
                description="case id",
                type=openapi.TYPE_STRING,
                required=True,
            )
        ],
        responses={status.HTTP_200_OK: OrdersSerializer},
    )
    def search(self, request):
        case_id = request.query_params.get("case_id")
        cases = Cases.objects.filter(case_id=case_id).first()
        orders = Orders.objects.filter(case=cases).all()
        if orders:
            serializer = OrdersSerializer(orders, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class OrdersViewSet2(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer2
    http_method_names = ["post"]
    
class CasesViewSet(viewsets.ModelViewSet):
    queryset = Cases.objects.all()
    serializer_class = CasesSerializer
    http_method_names = ["get", "post", "options"]


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    http_method_names = ["get", "post", "options"]


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer
    http_method_names = ["get", "post", "options"]

    @action(detail=False, methods=["GET"])
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="company_name",
                in_=openapi.IN_QUERY,
                description="client name",
                type=openapi.TYPE_STRING,
                required=True,
            )
        ],
        responses={status.HTTP_200_OK: ClientsSerializer},
    )
    def search(self, request):
        company_name = request.query_params.get("company_name")
        client = Clients.objects.filter(company_name=company_name).all()
        if client:
            serializer = ClientsSerializer(client, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SignupViewSet(viewsets.ModelViewSet):
    queryset = SalesPeople.objects.all()
    serializer_class = SignupSerializer
    http_method_names = ["post"]


class SalepeopleViewSet(viewsets.ModelViewSet):
    queryset = SalesPeople.objects.all()
    serializer_class = SignupSerializer
    http_method_names = ["get"]

    @action(detail=False, methods=["GET"])
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="name",
                in_=openapi.IN_QUERY,
                description="saleperson name",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                name="grade",
                in_=openapi.IN_QUERY,
                description="saleperson grade",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                name="account",
                in_=openapi.IN_QUERY,
                description="account",
                type=openapi.TYPE_STRING,
            ),
        ],
        responses={status.HTTP_200_OK: SignupSerializer},
    )
    def search(self, request):
        name = request.query_params.get("name")
        grade = request.query_params.get("grade")
        account = request.query_params.get("account")
        if account:
            saleperson = SalesPeople.objects.filter(account=account).all()
        elif not grade:
            saleperson = SalesPeople.objects.filter(name=name).all()
        else:
            saleperson = SalesPeople.objects.filter(name=name, grade=grade).all()
        if saleperson:
            serializer = SignupSerializer(saleperson, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class LoginViewSet(viewsets.ModelViewSet):
    queryset = SalesPeople.objects.all()
    serializer_class = LoginSerializer
    http_method_names = ["post"]

    def listed(self, request):
        token = request.data.get("token")
        token = Token.objects.filter(token=token).first()
        if token:
            pass
        else:
            return Response(
                {"error": "Not logged in"}, status=status.HTTP_401_UNAUTHORIZED
            )

    @swagger_auto_schema(responses={200: LoginTokenSerializer()})
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
    http_method_names = ["get", "post", "options"]
