from django.db import models
from django.contrib.auth.models import User

class recipe(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True,null=True)
    recipe_name = models.CharField(max_length = 20)
    recipe_discription = models.TextField()
    recipe_image = models.ImageField(upload_to = 'recipe_photos')

    def __str__(self):
        return self.recipe_name

