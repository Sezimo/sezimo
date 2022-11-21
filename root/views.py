from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse

# Generic Homepage like views that do no belong to an app.


class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {'app_name': reverse('root_index')}
        return render(request, "home/index.html", context=context)


class LoggedOutView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, "registration/logged-out.html", context={})
