from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from .models import NewsArticle
# Create your views here.


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        articles = NewsArticle.objects.all()
        context = {
            'articles': articles
        }
        return render(request, "news/index.html", context=context)
