from django.db import models

# Create your models here.


#when we create table we need to use the class keyword
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)   #similar to varchar and TextField similar to textarea
    
    def __str__(self):
        return self.name
    
class Student (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name