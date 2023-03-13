from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Comment
from django.core.paginator import Paginator


def article_details(request, slug):
    article = get_object_or_404(Article, slug=slug)

    if request.method == 'POST':
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article, user=request.user, parent=None)

    return render(request, 'blog/article_details.html', context={'article': article})


def articles_list(request):
    articles = Article.article_manager.published()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', context={'articles': objects_list, 'title': 'List of Articles'})


def category_details(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    category_articles = category.articles.all()
    page_number = request.GET.get('page')
    paginator = Paginator(category_articles, 2)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html',
                  context={'articles': objects_list, 'title': category.title + ' Category'})


def search_articles(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    objects_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', context={'articles': objects_list, 'title': 'Search Results for ' + q})
