from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from blogData.models import Article, Comment
from blogData.permission import IsCommentAuthorOrAdminWithin24h, IsAuthorOrAdmin
from blogData.serializers import ArticleListSerializer, ArticleDetailSerializer, CommentSerializer


# Create your views here.


# /articles
class ArticleListView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        # Serialize and return the articles
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# /articles/<int:id>
class ArticleDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Article, pk=pk)

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        permission = IsAuthorOrAdmin()
        if not permission.has_object_permission(request, self, article):
            raise PermissionDenied()
        serializer = ArticleDetailSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        permission = IsAuthorOrAdmin()
        if not permission.has_object_permission(request, self, article):
            raise PermissionDenied()
        article.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class CommentListCreateView(APIView):
    def get(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        Comments = article.comments.all()
        serializer = CommentSerializer(Comments, many=True)
        return Response(serializer.data)

    def post(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(article=article, author=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CommentDetailView(APIView):
    def get_object(self, article_pk, pk):
        article = get_object_or_404(Article, pk=article_pk)
        return get_object_or_404(Comment, pk=pk, article=article)

    def get(self, request, article_pk, pk):
        Comment = self.get_object(article_pk, pk)
        serializer = CommentSerializer(Comment)
        return Response(serializer.data)

    def put(self, request, article_pk, pk):
        comment = self.get_object(article_pk, pk)
        permission = IsCommentAuthorOrAdminWithin24h()
        if not permission.has_object_permission(request, self, comment):
            raise PermissionDenied(permission.message)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, article_pk, pk):
        comment = self.get_object(article_pk, pk)
        permission = IsCommentAuthorOrAdminWithin24h()
        if not permission.has_object_permission(request, self, comment):
            raise PermissionDenied(permission.message)
        comment.delete()
        return Response(status=HTTP_204_NO_CONTENT)
