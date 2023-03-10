from blog.models import Article, Category


def recent_articles(request):
    recent_articles_ = Article.article_manager.published().order_by('-created', '-updated')[:3]
    return {'recent_articles': recent_articles_}


def categories(request):
    categories_ = Category.objects.all().order_by('title')
    return {'categories': categories_}
