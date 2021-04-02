from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import Product, Review
from ..serializers import ProductSerializer, ReviewSeralizer

from rest_framework import status


@api_view('GET')
def getProducts(request):
    query = request.query_params.get('keyword')
    if query == None:
        query = ""
    products = Product.objects.filter(product_name__icontains=query).order_by('-created_at')
    page = request.query_params.get('page')
    paginator = Paginator(products, 6)

    try:
        products = paginator.page((page))
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    if page == None:
        page = 1

    page = int(page)
    print('Page', page)

    serializers = ProductSerializer(products, many=True)
    return Response({'products': serializers.data, 'page': page, "pages": paginator.num_pages})


@api_view(["POST"])
def createProduct(request):
    pass


@api_view(["POST"])
def updateProduct(request, pk):
    pass


@api_view(["Delete"])
def deleteProduct(request, pk):
    pass
