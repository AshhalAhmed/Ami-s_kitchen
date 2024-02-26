from django.db import models

# Create your models here.

class recipe(models.Model):
    recipe_name=models.CharField(max_length=100)
    recipe_text=models.TextField()
    recipe_picture=models.ImageField(upload_to="recipe_FOLDER")