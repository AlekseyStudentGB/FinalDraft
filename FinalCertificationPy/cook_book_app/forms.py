from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import *

class AddRecipe(forms.Form):

    title = forms.CharField(max_length=100, label='Название рецепта', widget=forms.TextInput(
        attrs={'class': 'name_class', 'placeholder': 'введите название рецепта', 'size': 100}, ))
    description = forms.CharField(label='Описание рецепта', widget=forms.Textarea(
        attrs={'class': 'name_class', 'placeholder': 'введите описание блюда'}))
    stages = forms.CharField(label='Этапы приготовления', widget=forms.Textarea(
        attrs={'class': 'name_class', 'placeholder': 'введите этапы приготовления блюда'}))
    time_preparations = forms.IntegerField(label='Время приготовления')
    img = forms.ImageField()
    categories = forms.ChoiceField(choices=[(ct.id, ct.title)for ct in Categories.objects.all()])

    def clean_name(self):
        name = self.cleaned_data['title']
        if len(name) < 3:
            raise forms.ValidationError('название рецепта должно быть больше 3 символов')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 1:
            raise forms.ValidationError('заполните описание')
        return description

    def clean_stages(self):
        stages = self.cleaned_data['stages']
        if len(stages) < 1:
            raise forms.ValidationError('заполните этапы приготовления')
        return stages


class ChRecipe(forms.Form):
    title = forms.CharField(required=False, min_length=0, max_length=100, label='Название рецепта', widget=forms.TextInput(
        attrs={'class': 'name_class', 'placeholder': 'введите название рецепта', 'size': 100}, ))
    description = forms.CharField(required=False, min_length=0, label='Описание рецепта', widget=forms.Textarea(
        attrs={'class': 'name_class', 'placeholder': 'введите описание блюда'}))
    stages = forms.CharField(required=False, min_length=0, label='Этапы приготовления', widget=forms.Textarea(
        attrs={'class': 'name_class', 'placeholder': 'введите этапы приготовления блюда'}))
    time_preparations = forms.IntegerField(required=False, label='Время приготовления')
    img = forms.ImageField(required=False)
    categories = forms.ChoiceField(choices=[(ct.id, ct.title)for ct in Categories.objects.all()])
class AddCt(forms.Form):
    title = forms.CharField()


class RegUser(forms.Form):
    name = forms.CharField(label="Имя")
    password = forms.CharField(label="Имя", widget=forms.PasswordInput())



