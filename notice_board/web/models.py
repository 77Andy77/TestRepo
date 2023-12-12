from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Categories(models.Model):
    title = models.TextField(max_length=256)


class advertisemenst(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=256)
    create_at = models.DateTimeField()
    price = models.FloatField()
    description = models.TextField(max_length=256)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)