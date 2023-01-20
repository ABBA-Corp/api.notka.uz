from rest_framework import serializers
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from .models import Product, ProductCategory, Banners


class ProductListSerializer(serializers.ModelSerializer):
    thumbnail_photo = HyperlinkedSorlImageField(
        '752x350',
        options={"crop": "center"},
        source='photo',
        read_only=True
    )

    class Meta:
        model = Product
        fields = ("name", "artikul", "thumbnail_photo",)


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductTopListSerializer(serializers.ModelSerializer):
    thumbnail_packaging = HyperlinkedSorlImageField(
        '752x350',
        options={"crop": "center"},
        source='packaging_photo',
        read_only=True
    )

    class Meta:
        model = Product
        fields = ("name", "weight", "artikul", "carbohydrates", "thumbnail_packaging")


class ProductBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = "__all__"
