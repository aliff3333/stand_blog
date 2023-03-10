from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('list', views.articles_list, name='articles_list'),
    path('details/<slug:slug>', views.article_details, name='article_details'),
    path('category/<int:pk>', views.category_details, name='category_details'),
]
