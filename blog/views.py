from django.shortcuts import render, get_object_or_404
from .models import Article


def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    recent_articles = Article.article_manager.published()[:3]
    return render(request, 'blog/article_details.html', context={
        'article': article, 'recent_articles': recent_articles})


def articles_list(request):
    articles = Article.article_manager.published()
    return render(request, 'blog/articles_list.html', context={'articles': articles})
