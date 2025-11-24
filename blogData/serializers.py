from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField
from .models import Article, Comment


class ArticleListSerializer(ModelSerializer):
    author = StringRelatedField(read_only=True)
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'created_at', 'updated_at']

class ArticleDetailSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content']

class CommentSerializer(ModelSerializer):
    # Les champs en lecture seule car ils sont gérés automatiquement
    author = StringRelatedField(read_only=True)
    article = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'