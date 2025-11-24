from django.urls import path

from blogData.views import ArticleListView, ArticleDetailView, CommentListCreateView, CommentDetailView

#blogData/urls.py

urlpatterns = [
    path('articles/', ArticleListView.as_view()),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('articles/<int:article_pk>/comments/', CommentListCreateView.as_view(), name='Comment-list-create'),
    path('articles/<int:article_pk>/comments/<int:pk>', CommentDetailView.as_view(), name='Comment-detail'),
]