from django.urls import include, path
from .views import IndexView

app_name = 'news'  # pylint: disable=invalid-name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/', include('news.api.urls')),
]
