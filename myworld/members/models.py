from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Members(models.Model):
    x=[('Male','Male'),('Female','Female')]
    y= [('Active','Active'),('Inactive','Inactive')] 
    a = [('IS','IS'),('CS','CS'),('AI','AI'),('DS','DS'),('IT','IT')]
    b = [('1','1'),('2','2'),('3','3'),('4','4')]
    Name = models.CharField(max_length=200, null=True)
    ID = models.PositiveIntegerField(primary_key=True)
    Gpa = models.DecimalField(max_digits=3, decimal_places=2, validators=[MaxValueValidator(4), MinValueValidator(0)])
    Level = models.CharField(max_length=20,choices=b)
    Department = models.CharField(max_length=20,choices=a)
    Status = models.CharField(max_length=20,choices=y)
    Gender = models.CharField(max_length=20,choices=x)
    Phone = models.CharField(max_length=200, null=True)
    Email = models.EmailField(max_length=254)
    Birth_Date = models.DateField(auto_now=False, auto_now_add=False)
    def _str_(self):
        return str(self.ID)
# Create your models here.
