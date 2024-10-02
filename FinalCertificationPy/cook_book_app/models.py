from django.db import models

# Create your models here.


class Categories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name: str = 'Категория'
        verbose_name_plural: str = 'Категории'


class Recipes(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    stages = models.TextField()
    time_preparations = models.IntegerField()
    img = models.ImageField(upload_to='recipes_img', blank=True)
    author = models.CharField(max_length=100, blank=True)
    categories = models.ForeignKey(Categories, blank=True, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name: str = 'Рецепт'
        verbose_name_plural: str = 'Рецепты'



