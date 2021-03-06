from django.urls import path

from .views import ShopListView, ShopDetailUpdateView, CategoryListView, CategoryDetailView, ProductListView, ProductDetailView


urlpatterns = [
    path ('', ShopListView.as_view()),
    path('<int:pk>/', ShopDetailUpdateView.as_view()),
    path('<int:shop_id>/categories/', CategoryListView.as_view()),
    path('<int:shop_id>/categories/<int:id>/', CategoryDetailView.as_view()),
    path('<int:shop_id>/categories/<int:cat_id>/products/', ProductListView.as_view()),
    path('<int:shop_id>/categories/<int:cat_id>/products/<int:id>/', ProductDetailView.as_view()),
]