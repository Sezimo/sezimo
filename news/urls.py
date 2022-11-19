from django.contrib import admin
from django.urls import include, path
from .views import IndexView

app_name = 'news'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
