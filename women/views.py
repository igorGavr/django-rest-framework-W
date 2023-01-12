from rest_framework import generics
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women, Category
from .serializers import WomenSerializer
from rest_framework import viewsets


class WomenViewSet(viewsets.ModelViewSet):
    # queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Women.objects.all()[:3]
        return Women.objects.filter(pk=pk)


    # додавання нового маршруту http://127.0.0.1:8000/api/v1/women/3/category/
    # який повертає нам назву категорії
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})





# class WomenApiList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
