from django.contrib import admin
from .models import NewsArticle
# Register your models here.


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    """Admin Form for News Article CRUD"""
    pass  # pylint: disable=unnecessary-pass
