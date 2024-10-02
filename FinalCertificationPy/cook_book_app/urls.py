from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('addrecipes/', add_recipes, name='add_recipes'),
    path('recipes/', get_recipes, name='get_recipes'),
    path('recipe/<int:pk>', get_recipe, name='get_recipe'),
    path('changerecipe/<int:pk>', change_recipe, name='change_recipe'),
    path('addct', add_categories, name='add_categories'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
