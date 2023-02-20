from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product

from .cart import Cart


# Create your views here.
class CartView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(operation_summary="Retrieves items in the cart")
    def get(self, request, *args, **kwargs):
        user_cart = Cart(request)
        if user_cart.cart:
            data = []
            for item in user_cart:
                data.append(item)
            return Response(
                {
                    "Cart items": data,
                    "Items count": len(user_cart),
                    "Total cost": user_cart.get_total_cost(),
                },
                status=status.HTTP_200_OK,
            )
        return Response({"message": "Your cart is empty"}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="Updates an item in the cart",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["product_name", "quantity"],
            properties={
                "product_name": openapi.Schema(type=openapi.TYPE_STRING),
                "quantity": openapi.Schema(type=openapi.TYPE_INTEGER),
            },
            example={"product_name": "quantity"},
        ),
    )
    def put(self, request, *args, **kwargs):
        """
        Updates an item in the cart with a new quantity if the product exists in the cart
        """
        data = request.data
        user_cart = Cart(request)
        for key, value in data.items():
            product = get_object_or_404(Product, name=key)
            if str(product.id) in user_cart.cart.keys():
                user_cart.update_item(product, quantity=value)
                return Response({"message": "Cart updated"}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"message": "This item is not in your cart"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

    @swagger_auto_schema(
        operation_summary="Removes an item from cart or clears the cart",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "product_name": openapi.Schema(type=openapi.TYPE_STRING),
            },
            example={"product_name": ""},
        ),
    )
    def delete(self, request, *args, **kwargs):
        """
        Removes an item from the cart if item is specified in request body, else the cart will be cleared
        """
        data = request.data
        user_cart = Cart(request)
        if data:
            for key in data.keys():
                product = get_object_or_404(Product, name=key)
                removed = user_cart.remove_item(product)
                if removed:
                    return Response(
                        {"message": "Item has been removed from cart"},
                        status=status.HTTP_200_OK,
                    )
                else:
                    return Response(
                        {"message": "This item is not in your cart"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
        user_cart.clear()
        return Response(
            {"message": "Cart has been cleared"}, status=status.HTTP_204_NO_CONTENT
        )
