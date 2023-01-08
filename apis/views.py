from rest_framework.response import Response

from . import models, serializers
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_products(request, *args, **kwargs):
    products = models.Product.objects.all()
    data = serializers.ProductSerializer(products, many=True).data
    return Response(data)


@api_view(['GET'])
def get_product_by_id(request, *args, **kwargs):
    product = models.Product.objects.get(id=int(kwargs["id"]))
    data = serializers.ProductSerializer(product).data
    return Response(data)


@api_view(['GET'])
def get_categories(request, *args, **kwargs):
    categories = models.Category.objects.all()
    data = serializers.CategorySerializer(categories, many=True).data
    return Response(data)


@api_view(['GET'])
def get_category_by_id(request, *args, **kwargs):
    category = models.Category.objects.get(id=int(kwargs["id"]))
    data = serializers.CategorySerializer(category).data

    return Response(data)


@api_view(['GET'])
def get_products_by_category(request, *args, **kwargs):
    category_name = models.Category.objects.get(id=int(kwargs["id"])).name
    products = models.Product.objects.filter(product_category=category_name)
    data = serializers.ProductSerializer(products, many=True).data
    return Response(data)
