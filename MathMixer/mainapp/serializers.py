from rest_framework import serializers
from .models import Category, Charackterstick, Product

class CharackterstickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charackterstick
        fields = ['charackterstick1', 'charackterstick2', 'charackterstick3', 'charackterstick4', 'charackterstick5']

class CategorySerializer(serializers.ModelSerializer):
    charackterstick = CharackterstickSerializer()

    class Meta:
        model = Category
        fields = ['id_category', 'name', 'charackterstick']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'textdes', 'category']

class ProductаSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id_product', 'name', 'average_rating']  # Добавьте другие поля по необходимости

    def get_average_rating(self, obj):
        total_rating = obj.rating1 + obj.rating2 + obj.rating3 + obj.rating4 + obj.rating5
        average = total_rating / 5
        return average

class CharackterstickDiscSerializer(serializers.ModelSerializer):
    class Meta:
        model = Charackterstick
        fields = [
            'charackterstick1',
            'charackterstick2',
            'charackterstick3',
            'charackterstick4',
            'charackterstick5',
        ]

class CategoryDiscSerializer(serializers.ModelSerializer):
    charackterstick = CharackterstickDiscSerializer()

    class Meta:
        model = Category
        fields = ['name', 'charackterstick']

class ProductDetailSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    category = CategoryDiscSerializer()

    class Meta:
        model = Product
        fields = [
            'id_product',
            'name',
            'textdes',
            'average_rating',
            'category',
        ]

    def get_average_rating(self, obj):
        total_rating = obj.rating1 + obj.rating2 + obj.rating3 + obj.rating4 + obj.rating5
        average = total_rating / 5
        return average