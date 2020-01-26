from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetailView, GenericAPIView

urlpatterns = [
    #path('article/', article_list),
    #path('detail/<int:pk>', article_detail),
    path('article/', ArticleAPIView.as_view()),
    path('article/<int:id>', ArticleDetailView.as_view()),
    path('generic/article/<int:id>', GenericAPIView.as_view()),
    path('generic/article/', GenericAPIView.as_view()),
]
