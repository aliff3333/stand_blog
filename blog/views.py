from django.shortcuts import render, get_object_or_404
from .models import Article


def article_details(request, pk):
    article = get_object_or_404(Article, id=pk)
    return render(request, 'blog/article_details.html', context={'article': article})
