from django.shortcuts import render
from rest_framework import generics
from .models import Company
from .serializers import CompanySerializer
from rest_framework.pagination import PageNumberPagination

class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    pagination_class = PageNumberPagination
    page_size = 10
    page_size_query_param = 'page_size'
    
    
    
class CompanyRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer