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
        
from .models import Comment
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'created_at']
        read_only_fields = ['user']