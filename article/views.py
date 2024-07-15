from django.shortcuts import render

from rest_framework import generics

from rest_framework.permissions import IsAuthenticated,AllowAny

from .models import Article
from .serializer import ArticleSerializer
from .permissions import IsOwnerOrReadOnly


class RetrieveArticle(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'

class ListArticle(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [AllowAny]

class CreateArticle(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DeleteArticle(generics.DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'pk'


class UpdateArticle(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    lookup_field = 'pk'


class PrivateArticleList(generics.ListAPIView):
    queryset = Article.objects.filter(is_public=False)
    serializer_class = ArticleSerializer


class PrivateRetrieveArticle(generics.RetrieveAPIView):
    queryset = Article.objects.filter(is_public=False)
    serializer_class = ArticleSerializer
    lookup_field = 'pk'
