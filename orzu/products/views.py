from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Product, ProductCategory, Banners
from .serializers import (
    ProductListSerializer, ProductDetailSerializer,
    ProductCategorySerializer, ProductBannerSerializer
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category", "country")
    list_serializer_class = ProductListSerializer
    serializer_class = ProductDetailSerializer
    filterset_fields = ["category_id", "country_id", "is_top"]
    http_method_names = ["get"]

    def get_serializer_class(self):
        if self.action == "list":
            return self.list_serializer_class
        return self.serializer_class


class ProductCategoryListView(mixins.ListModelMixin,
                            GenericViewSet):
    queryset = ProductCategory.objects.all().order_by('pk')
    serializer_class = ProductCategorySerializer


class ProductBannerListView(mixins.ListModelMixin,
                            GenericViewSet):
    queryset = Banners.objects.all()
    serializer_class = ProductBannerSerializer
