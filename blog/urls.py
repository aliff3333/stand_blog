from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('details/<int:pk>', views.article_details, name='article_details')
]