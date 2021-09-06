from django.db import models

# Create your models here.
class company(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class User(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=20)
    c_name = models.ForeignKey(company,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
#  many to many relationship
class order(models.Model):
    id = models.AutoField
    o_name = models.CharField(max_length=55)

    def __str__(self):
        return self.o_name

class customer(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=66)
    order_name = models.ManyToManyField(order)

    def __str__(self):
        return self.name