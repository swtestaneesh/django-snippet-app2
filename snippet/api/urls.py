from posixpath import basename
from django.conf.urls import url, include
from .views import ProductViewSet, SalesViewSet, SnippetsViewSet, TagsViewSet,SalesApiView
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register("snippet", SnippetsViewSet, basename="snippet")
router.register("product", ProductViewSet, basename="products")
router.register("sale", SalesViewSet, basename="sales")
router.register("tag", TagsViewSet, basename="tag")


urlpatterns = [
    url('', include(router.urls)),
    path('sale-new/<product_id>', SalesApiView.as_view(),name="sale-new"),
    path('sale-new/<int:pk>', SalesApiView.as_view()),
]
