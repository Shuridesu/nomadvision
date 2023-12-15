from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Post,Category
from .serializers import IndexSerializer,CategorySerializer

class LatestPostsView(ListAPIView):
    serializer_class = IndexSerializer
    queryset = Post.objects.all().order_by('-pub_date')

class RecommendedPostsView(ListAPIView):
    serializer_class = IndexSerializer
    queryset = Post.objects.filter(is_recommended=True)
    
class TrendsAiPostsView(ListAPIView):
    serializer_class = IndexSerializer
    queryset = Post.objects.filter(is_trends_ai=True)
    
class TrendsDataPostsView(ListAPIView):
    serializer_class = IndexSerializer
    queryset = Post.objects.filter(is_trends_data=True)
    
class IndustryAnalyticsPostsView(ListAPIView):
    serializer_class = IndexSerializer
    queryset = Post.objects.filter(is_industry_insights=True)
    
class AiSoftwarePostsView(ListAPIView):
    serializer_class = IndexSerializer
    queryset = Post.objects.filter(is_ai_software=True)
    
from rest_framework.response import Response

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = IndexSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # 前後の記事を取得
        prev_instance = Post.objects.filter(id__lt=instance.id).order_by('-id').first()
        next_instance = Post.objects.filter(id__gt=instance.id).order_by('id').first()
        prev_serializer = self.get_serializer(prev_instance)
        next_serializer = self.get_serializer(next_instance)

        # レスポンスに前後の記事を含める
        return Response({
            'post': serializer.data,
            'previous': prev_serializer.data if prev_instance else None,
            'next': next_serializer.data if next_instance else None
        })

    

class PostCategoryView(ListAPIView):
    serializer_class = IndexSerializer
    def get_queryset(self):
        category_slug = self.kwargs['category']
        return Post.objects.filter(category__slug=category_slug)
 
class CategoryView(ListAPIView):
     serializer_class = CategorySerializer
     queryset = Category.objects.all()