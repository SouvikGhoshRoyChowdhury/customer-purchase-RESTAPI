from rest_framework import serializers

from .models import Product


class ProductsSerializer(serializers.ModelSerializer):
    """
    Products Serializer To Filter Fields And Serializes From Product Model
    """

    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = [
            "name",
            "category",
            "description",
            "stock",
            "price",
            "sold",
        ]


class ProductInstanceSerializer(ProductsSerializer):
    """
    Products Serializer To Filter Fields Of Each Product
    """

    class Meta:
        model = Product
        fields = ProductsSerializer.Meta.fields


class SimpleProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = [
            "name",
            "category",
            "price",
        ]
