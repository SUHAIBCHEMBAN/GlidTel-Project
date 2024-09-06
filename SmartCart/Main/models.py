from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    discription = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Product_img',default='default.img')
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.name

