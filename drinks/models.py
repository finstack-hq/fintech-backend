from django.db import models

# Create your models here.
class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name + '' + self.description

class Currency(models.Model):
    result = models.CharField(max_length=200)
    base_code = models.CharField(max_length=50)
    EUR = models.CharField(max_length=200)
    GBP = models.CharField(max_length=200)
    USD = models.CharField(max_length=200)

    def __str__(self):
        return self.result + '' + self.base_code + '' + self.EUR + '' + self.GBP + '' + self.USD
    
