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
from accounts.serializers import UserSerializer
class CommentSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(
        queryset=Post.objects.all(),
        slug_field='slug'
    )
    user=UserSerializer(read_only=True)
    parent = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=False, allow_null=True)
    class Meta:
        model = Comment
        fields = "__all__"
    
    def create(self, validated_data):
        """
        `parent`フィールドが提供されている場合は、返信コメントとして作成します。
        提供されていない場合は、通常のコメントとして扱います。
        """
        return Comment.objects.create(**validated_data)