from rest_framework import serializers
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from .models import Product, ProductCategory, Banners


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductCategorySerializer(serializers.ModelSerializer):
    thumbnail_landscape = HyperlinkedSorlImageField(
        '752x350',
        options={"crop": "center"},
        source='landscape_photo',
        read_only=True
    )
    thumbnail_photo = HyperlinkedSorlImageField(
        '400x600',
        options={"crop": "center"},
        source='photo',
        read_only=True
    )

    class Meta:
        model = ProductCategory
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    thumbnail_packaging = HyperlinkedSorlImageField(
        '752x350',
        options={"crop": "center"},
        source='packaging_photo',
        read_only=True
    )
    thumbnail_photo = HyperlinkedSorlImageField(
        '752x350',
        options={"crop": "center"},
        source='photo',
        read_only=True
    )

    class Meta:
        model = Product
        fields = "__all__"


class ProductBannerSerializer(serializers.ModelSerializer):
    thumbnail_photo = HyperlinkedSorlImageField(
        '752x350',
        options={"crop": "center"},
        source='photo',
        read_only=True
    )

    class Meta:
        model = Banners
        fields = "__all__"
