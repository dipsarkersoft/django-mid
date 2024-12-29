from django.db import models
from django.contrib.auth.models import User





class BrandModel(models.Model):
    name=models.CharField(max_length=30)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Car_Model(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=200)
    price=models.IntegerField()
    quantity=models.IntegerField()
    brand=models.ForeignKey(BrandModel,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='mainapp/media/uploads/', blank = True, null = True)
    
    def __str__(self):
        return self.name



class OrderModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    car=models.ForeignKey(Car_Model,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.car.name} by {self.user.username}"
    


class Comment(models.Model):
    car = models.ForeignKey(Car_Model, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"