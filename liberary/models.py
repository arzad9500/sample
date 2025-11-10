from django.db import models


class Book(models.Model):

    title       = models.CharField(max_length=150,null=True)
    description = models.TextField()

    def __str__(self):
    
        return self.title

class laptop(models.Model): # this need serilizers

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100,null = True)  # this is null so this is optional

    def __str__(self):
        return self.brand