from django.shortcuts import render, get_object_or_404
from .models import Article, Category


def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)
    recent_articles = Article.article_manager.published()[:3]
    return render(request, 'blog/article_details.html', context={'article': article})


def articles_list(request):
    articles = Article.article_manager.published()
    return render(request, 'blog/articles_list.html', context={'articles': articles, 'title': 'List of Articles'})


def category_details(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    category_articles = category.articles.all()
    return render(request, 'blog/articles_list.html',
                  context={'articles': category_articles, 'title': category.title + ' Category'})
