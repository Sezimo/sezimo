from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView

# Create your views here.


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {'app_name': reverse('news:index')}
        return render(request, "news/index.html", context=context)
