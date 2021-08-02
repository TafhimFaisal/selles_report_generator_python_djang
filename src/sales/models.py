from django.db import models
from products.models import Product
from customers.models import Customer
from profiles.models import Profile
from django.utils import timezone
from .utils import generate_code

# Create your models here.
class Possition(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)
    def __str__(self):
        return f"ID: {self.id}, Product: {self.product.name}, Quantity: {self.quantity}"
    
    def save(self, *args,**kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args,**kwargs)
    

class Sale(models.Model):
    transation_id = models.CharField(max_length=12,blank=True)
    possition = models.ManyToManyField(Possition)
    totat_price = models.FloatField(blank=True,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    seles_man = models.ForeignKey(Profile,on_delete=models.CASCADE)
    craeted = models.DateTimeField(blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Seles for the amout of {self.totat_price} "

    def save(self, *args,**kwargs):
        if self.transation_id == "":
            self.transation_id = generate_code()
        if self.craeted is None:
            self.craeted = timezone.now()
        return super().save(*args,**kwargs)

    def get_position(self):
        return self.possition.all()

class CSV(models.Model):
    file_name = models.FileField(upload_to='csvs')
    activated = models.BooleanField(default=True)
    craeted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.file_name)