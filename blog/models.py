from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(published=True)


class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='articles')
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images/articles')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, unique=True)

    # managers
    objects = models.Manager()
    article_manager = ArticleManager()

    class Meta:
        ordering = ('-created', '-updated')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return reverse('blog:article_details', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title} | {self.body[:30]}"


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)

    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.user.username} | {self.body[:50]}'

