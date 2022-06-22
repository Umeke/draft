from rest_framework import serializers



from shop.models import Shop, Category, Product


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'shop_name',)


class CategorySerializer(serializers.ModelSerializer):
    # shop_name = ShopSerializer()
    class Meta:
        model = Category
        fields = ('id', 'cat_name')


class ProductSerializer(serializers.ModelSerializer):
    # cat_name = CategorySerializer()
    # shop_name = ShopSerializer()

    class Meta:
        model = Product
        fields = ('id', 'product_name')

