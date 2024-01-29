from django.db import models

# Create your models here.
class Food(models.Model):
    food_name = models.CharField(max_length=50)
    food_price = models.IntegerField()
    food_code = models.IntegerField(primary_key=True)
    food_off_code = models.CharField(max_length=3, default=0)
    food_description = models.TextField()
    food_image = models.ImageField(default='default.png', upload_to='food_images/')


    def __str__(self):
        return self.food_name

class Section(models.Model):
    section_name = models.CharField(max_length=50)
    section_code = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.section_name

class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_phone = models.IntegerField(primary_key=True)
    customer_address = models.TextField(null=False)

    def __str__(self):
        return self.customer_name
'''    
class Address(models.Model):
    customer_phone = models.IntegerField(primary_key=True)
    address.street = models.TextField
    address.plaque = models.IntegerField
'''
class Factor(models.Model):
    factor_number = models.IntegerField(primary_key=True)
    factor_datetime = models.DateTimeField

    def __str__(self):
        return self.factor_number

class Select(models.Model):
    select_number = models.IntegerField
    factor_number = models.ForeignKey
    food_code = models.ForeignKey

    def __str__(self):
       return self.select_number
   
   

class BikeDelivery(models.Model):
    bikedelivery_code = models.IntegerField(primary_key=True)
    bikedelivery_name = models.CharField(max_length=50)
    bikedelivery_phone = models.IntegerField()
    
    
    def __str__(self):
        return self.bikedelivery_code

