from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.


class NewsArticle(models.Model):
    """News Article Model"""
    title = models.CharField(max_length=50, blank=False, null=False)
    short_description = models.TextField(blank=True, null=True)
    content = RichTextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    spotlight = models.BooleanField(default=False)
    spotlight_expiry = models.DateTimeField(null=True, blank=True)
    create_dttm = models.DateTimeField(auto_now_add=True, editable=False)
    updated_dttm = models.DateTimeField(auto_now=True, editable=False)
