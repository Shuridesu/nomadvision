from rest_framework.generics import ListAPIView,RetrieveAPIView
from .models import Post,Category
from .serializers import IndexSerializer,CategorySerializer
from rest_framework.permissions import AllowAny

class LatestPostsView(ListAPIView):
    serializer_class = IndexSerializer
    queryset = Post.objects.all().order_by('-pub_date')
    permission_classes = (AllowAny,)

class RecommendedPostsView(ListAPIView):
    serializer_class = IndexSerializer
    queryset = Post.objects.filter(is_recommended=True)
    permission_classes = (AllowAny,)
    
class TrendsAiPostsView(ListAPIView):
    serializer_class = IndexSerializer
    queryset = Post.objects.filter(is_trends_ai=True)
    permission_classes = (AllowAny,)
    
class TrendsDataPostsView(ListAPIView):
    serializer_class = IndexSerializer
    queryset = Post.objects.filter(is_trends_data=True)
    permission_classes = (AllowAny,)
    
class IndustryAnalyticsPostsView(ListAPIView):
    serializer_class = IndexSerializer
    queryset = Post.objects.filter(is_industry_insights=True)
    permission_classes = (AllowAny,)
    
class AiSoftwarePostsView(ListAPIView):
    serializer_class = IndexSerializer
    queryset = Post.objects.filter(is_ai_software=True)
    permission_classes = (AllowAny,)
    
from rest_framework.response import Response

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = IndexSerializer
    permission_classes = (AllowAny,)
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
    permission_classes = (AllowAny,)
    def get_queryset(self):
        category_slug = self.kwargs['category']
        return Post.objects.filter(category__slug=category_slug)
 
class CategoryView(ListAPIView):
     serializer_class = CategorySerializer
     queryset = Category.objects.all()
     permission_classes = (AllowAny,)
     
# views.py
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

class ContactView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        subject = "from nomadvision's client"
        message = request.data.get('message')
        from_email = settings.EMAIL_HOST_USER  # 送信元メールアドレス
        user_email = request.data.get('email')  # ユーザーのメールアドレス

        email = EmailMessage(
            subject,
            message,
            from_email,
            [settings.DEFAULT_TO_EMAIL],  # 受信者メールアドレス
            headers={'Reply-To': user_email}
        )

        try:
            email.send()
            return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


