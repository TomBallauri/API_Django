from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey, CASCADE
from apiBlog import settings


# Create your models here.
class Article(Model):
    title = CharField(max_length=512)
    content = TextField()
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

class Comment(Model):
    content = TextField()
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    article = ForeignKey(Article, on_delete=CASCADE, related_name='comments')