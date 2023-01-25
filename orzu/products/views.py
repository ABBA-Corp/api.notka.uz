from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

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


class ProductCategoryListView(APIView):
    @extend_schema(responses={200: ProductCategorySerializer(many=True)})
    def get(self, request):
        products = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(products, many=True)
        return Response(serializer.data)


class ProductBannerListView(APIView):
    @extend_schema(responses={200: ProductBannerSerializer(many=True)})
    def get(self, request):
        banners = Banners.objects.all()
        serializer = ProductBannerSerializer(banners, many=True)
        return Response(serializer.data)
