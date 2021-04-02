from django.db import models
from django import forms
# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.title
class Job(models.Model):
    title=models.CharField(max_length=100)
    skills=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    salary=models.FloatField(null=True)
    publish_date=models.DateField(auto_now=True)
    expire_date=models.DateField()
    description=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='job',null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        db_table="job"