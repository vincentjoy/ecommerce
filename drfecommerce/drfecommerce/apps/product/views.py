from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer


class CategoryView(viewsets.ViewSet):
    """
    A simple view set for viewing categories
    """

    queryset = Category.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)