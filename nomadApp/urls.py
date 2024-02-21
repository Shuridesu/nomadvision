from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('posts/latest/', views.LatestPostsView.as_view(), name='latest-posts'),
    path('posts/recommended/', views.RecommendedPostsView.as_view(), name='recommended-posts'),
    path('posts/ai-trends/', views.TrendsAiPostsView.as_view(), name='ai-trends-posts'),
    path('posts/data-trends/', views.TrendsDataPostsView.as_view(), name='data-trends-posts'),
    path('posts/industry-analytics/', views.IndustryAnalyticsPostsView.as_view(), name='industry-analytics'),
    path('posts/ai-software/', views.AiSoftwarePostsView.as_view(), name='ai-software'),
    path('tag/<slug:category>/',views.PostCategoryView.as_view(), name = 'category'),
    path('tag/',views.CategoryView.as_view(),name = 'category'),
    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('send-email/', views.ContactView.as_view(), name='send_email'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('', include(router.urls)),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)