from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from random import choice
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import *


def index(request):
    recipes = list(Recipes.objects.all())
    random_recipes = []
    if len(recipes) > 5:
        for _ in range(5):
            recipe = choice(recipes)
            random_recipes.append(recipe)
            recipes.remove(recipe)
    else:
        random_recipes = recipes
    return render(request, 'cook_book_app/index.html', {'random_recipes': random_recipes})


def add_recipes(request):
    if request.method == 'POST':
        form = AddRecipe(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            stages = form.cleaned_data['stages']
            img = form.cleaned_data['img']
            time_preparations = form.cleaned_data['time_preparations']
            categories_id = int(form.cleaned_data['categories'])

            categories = Categories.objects.get(id=categories_id)
            recipe = Recipes(title=title,
                             description=description,
                             stages=stages,
                             time_preparations=time_preparations,
                             categories=categories)
            recipe.img = img

            recipe.save()
            return render(request, 'cook_book_app/add_success.html')
    form = AddRecipe()
    return render(request, 'cook_book_app/add_recipes.html', {"form": form})


def get_recipes(request):
    recipes = Recipes.objects.all()
    return render(request, 'cook_book_app/get_recipes.html', {"recipes": recipes})


def get_recipe(request, pk):
    recipe = Recipes.objects.filter(pk=pk).first()

    if request.method == 'POST':
        recipe.delete()
        return render(request, 'cook_book_app/add_success.html')

    return render(request, 'cook_book_app/get_recipe.html', {"recipe": recipe})


def change_recipe(request, pk):
    recipe = Recipes.objects.filter(id=pk).first()
    if request.method == 'POST':
        form = ChRecipe(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            if len(title) > 0:
                recipe.title = title
                recipe.save()
            return render(request, 'cook_book_app/add_success.html')
    form = ChRecipe()
    return render(request, 'cook_book_app/add_recipes.html', {"form": form})


def add_categories(request):
    if request.method == 'POST':
        form = AddCt(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            category = Categories(title=title)
            category.save()
            return render(request, 'cook_book_app/add_success.html')
    form = AddCt()
    return render(request, 'cook_book_app/add_recipes.html', {"form": form})


'''def login_us(request):
    return render(request, 'cook_book_app/login.html')


def registration_us(request):
    if request.method == 'POST':
        form = RegUser(request.POST)
        user = form.cleaned_data['name']
        password = form.cleaned_data['password']
        usr = authenticate()
    return render(request, 'cook_book_app/registration.html')'''

