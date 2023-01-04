from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
# from simple_mail.mail import send_mail

from app.models import *
from .serializer import *
from .pagination import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


# Create your views here.


# def productsPage(request, category_slug=None):
#     categories = None
#     products = None
#     if category_slug != None:
#         categories = get_object_or_404(Category, slug=category_slug)
#         products = Product.objects.filter(category=categories, is_available=True)
#         product_count = products.count()
#     else:
#         products = Product.objects.all().filter(is_available=True)
#         product_count = products.count()
#     context = {
#         'categories':categories,
#         'products':products,
#         'product_count':product_count,
#     }
#     return render(request, 'products.html', context)

# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 100
#     page_size_query_param = 'page_size'
#     max_page_size = 1000

# @api_view(['GET',])
# def api_products(request):
#     if request.method == "GET":
#         products = Product.objects.all()

#         # Set up pagination
#         paginator = PageNumberPagination()
#         paginator.page_size = 300
#         result_page = paginator.paginate_queryset(products, request)

#         # Serialize the result page
#         serializer = ProductSerializer(result_page, many=True)
#         return Response(serializer.data)

@api_view(['GET',])
def api_categories(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def getPhotos(request):
    if request.method == "GET":
        photo = Photo.objects.all()
        serializer = PhotoSerializer(photo, many=True)
        return Response(serializer.data)
