from django.contrib.auth.decorators import login_required
from django.urls import include, re_path, path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from order.views import *
from doc_login.views import *

schema_view = get_schema_view(
    openapi.Info(
        title="COLD order API",
        default_version="v1",
        description="API for bms monitor",
        terms_of_service="https://api.coldelectric.com",
        contact=openapi.Contact(email="ernielin@htbi.com.tw"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r"order", OrdersViewSet)
router.register(r"order2", OrdersViewSet2)
router.register(r"case", CasesViewSet)
router.register(r"pcs", PcsViewSet)
router.register(r"product", ProductsViewSet)
router.register(r"client", ClientsViewSet)
router.register(r"salepeople", SalepeopleViewSet)
router.register(r"login", LoginViewSet)
router.register(r"logout", LogoutViewSet)
router.register(r"signup", SignupViewSet)


urlpatterns = [
    path("doc/", verify_required(login_url='/login')(schema_view.with_ui("swagger", cache_timeout=0)), name="schema-doc"),
    path("redoc/", verify_required(login_url='/login')(schema_view.with_ui("redoc", cache_timeout=0)), name="schema-redoc"),
    re_path(r"^api/", include(router.urls)),
    path("login/", login_view, name="login"),  
    path("verify-code/", verify_code_view, name="verify-code"),
]
