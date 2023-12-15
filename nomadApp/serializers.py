from rest_framework import serializers
from .models import Post,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class IndexSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'