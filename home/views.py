from django.shortcuts import render
from blog.models import Article


def home(request):
    articles = Article.article_manager.published()
    recent_articles = Article.article_manager.published().order_by('-created', '-updated')[:3]
    return render(request, 'home/index.html', context={'articles': articles})


def sidebar(request):
    context = {'name': 'ali'}
    return render(request, 'includes/sidebar.html', context)
