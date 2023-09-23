from django.urls import include, re_path, path
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from order import views

router = DefaultRouter()
router.register(r"order", views.OrdersViewSet)
router.register(r"case", views.CasesViewSet)
router.register(r'pcs', views.PcsViewSet)
router.register(r"product", views.ProductsViewSet)
router.register(r"client", views.ClientsViewSet)
router.register(r"login", views.LoginViewSet)
router.register(r"logout", views.LogoutViewSet)
router.register(r"signup", views.SignupViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="COLD order API",
        default_version="v1",
        description="API for bms monitor",
        terms_of_service="https://coldelectric.ai",
        contact=openapi.Contact(email="ernielin@htbi.com.tw"),
        license=openapi.License(name="Awesome IP"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    path(
        "doc/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    re_path(r"^api/", include(router.urls)),
]
