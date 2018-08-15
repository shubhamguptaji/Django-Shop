from django.db import models

# Create your models her
class Categories(models.Model):
    cName = models.CharField(max_length=200)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.cName

class Items(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=50)
    image = models.CharField(max_length=500)
    sellerName = models.CharField(max_length=50)
    sellerAddress = models.CharField(max_length=100)
    sellerPhoneNumber = models.CharField(max_length=13)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

