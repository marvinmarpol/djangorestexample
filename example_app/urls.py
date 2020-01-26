from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetailView, GenericAPIView, ArticleViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewset, basename='article')

urlpatterns = [

    # routes using viewsets
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),

    #path('article/', article_list),
    #path('detail/<int:pk>', article_detail),
    path('article/', ArticleAPIView.as_view()),
    path('article/<int:id>', ArticleDetailView.as_view()),
    path('generic/article/<int:id>', GenericAPIView.as_view()),
    path('generic/article/', GenericAPIView.as_view()),
]
