from drf_spectacular.utils import extend_schema
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Product, ProductCategory
from .serializers import ProductListSerializer, ProductDetailSerializer, ProductCategorySerializer, \
    ProductTopListSerializer


class ProductPagination(PageNumberPagination):
    page_size = 10


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related("category", "country")
    pagination_class = ProductPagination
    list_serializer_class = ProductListSerializer
    serializer_class = ProductDetailSerializer
    filterset_fields = ["category_id", "country_id"]
    http_method_names = ["get"]

    def get_serializer_class(self):
        if self.action == "list":
            return self.list_serializer_class
        return self.serializer_class

    @extend_schema(responses={200: ProductTopListSerializer(many=True)})
    @action(detail=False)
    def tops(self, request):
        products = Product.objects.filter(is_top=True)
        serializer = ProductTopListSerializer(products, many=True)
        return Response(serializer.data)


class ProductCategoryListView(APIView):
    @extend_schema(responses={200: ProductCategorySerializer(many=True)})
    def get(self, request):
        products = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(products, many=True)
        return Response(serializer.data)
