from rest_framework import generics
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .models import Women, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer
from rest_framework import viewsets


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )



# class WomenViewSet(viewsets.ModelViewSet):
#     # queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#             return Women.objects.all()[:3]
#         return Women.objects.filter(pk=pk)
#
#
#     # додавання нового маршруту http://127.0.0.1:8000/api/v1/women/3/category/
#     # який повертає нам назву категорії
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})
