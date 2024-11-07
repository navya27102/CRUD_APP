from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=25,blank=False,null=True)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    position = models.CharField(max_length=25,blank=False,null=False)
    
    def __str__(self):
        return self.name