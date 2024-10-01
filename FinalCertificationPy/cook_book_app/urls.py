from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]
