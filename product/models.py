from django.db import models

# Create your models here.
# django orm --> Object Relational Mapping

class Product(models.Model):
    # We don't have to provide ID explicitly
    pName = models.CharField(max_length=100)
    pPrice = models.FloatField()
    pQty = models.IntegerField()
    pDes = models.CharField(max_length=100, null=True)
    pStatus = models.BooleanField(default=True)
    pColor = models.CharField(max_length=100,null=True)
    #if you don't provide table name in meta class product.product

    def __str__(self):
        return self.pName

    class Meta:
        db_table = 'products'

class Employee(models.Model):
    name = models.CharField(max_length=100)
    #email = varchar
    email = models.EmailField()
    password = models.CharField(max_length=100)
    salary = models.FloatField()
    age = models.PositiveIntegerField()
    joiningDate = models.DateField()
    birthDate = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employees'