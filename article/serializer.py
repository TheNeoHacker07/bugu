from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        article = super(ArticleSerializer, self).create(validated_data)
        article.save()
        return article
