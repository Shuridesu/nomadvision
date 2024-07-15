from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

router = DefaultRouter()
router.register(r'api/comments', CommentViewSet)

urlpatterns = [
    path('api/posts/latest/', views.LatestPostsView.as_view(), name='latest-posts'),
    path('api/posts/recommended/', views.RecommendedPostsView.as_view(), name='recommended-posts'),
    path('api/posts/ai-trends/', views.TrendsAiPostsView.as_view(), name='ai-trends-posts'),
    path('api/posts/data-trends/', views.TrendsDataPostsView.as_view(), name='data-trends-posts'),
    path('api/posts/industry-analytics/', views.IndustryAnalyticsPostsView.as_view(), name='industry-analytics'),
    path('api/posts/ai-softwares/', views.AiSoftwarePostsView.as_view(), name='ai-software'),
    path('api/tag/<slug:category>/',views.PostCategoryView.as_view(), name = 'category'),
    path('api/tag/',views.CategoryView.as_view(),name = 'category'),
    path('api/posts/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('api/send-email/', views.ContactView.as_view(), name='send_email'),
    path('api/search/', views.SearchView.as_view(), name='search'),
    path('', include(router.urls)),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)