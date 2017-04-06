from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()
    count = models.IntegerField(default=0)
    usage = models.BooleanField()

    def __str__(self):
        return self.name