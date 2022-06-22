from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView

from rest_framework import mixins

from rest_framework import generics

from shop.models import Shop, Category,Product

from shop.serializers import ShopSerializer, CategorySerializer, ProductSerializer


class ShopListView(ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopDetailUpdateView(RetrieveUpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class CategoryListView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShopList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


