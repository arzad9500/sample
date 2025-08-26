from django.db import models

# Create your models here.
class Student(models.Model):
    name     = models.CharField(max_length=100)
    age      = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Task (models.Model):

    student_reference = models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    task_name   = models.CharField(max_length=150)
    description = models.TextField()


class Ranksheet(models.Model):
    tamil   = models.IntegerField()
    english = models.IntegerField()
    maths   = models.IntegerField()
    science = models.IntegerField()
    social  = models.IntegerField()
    total   = models.IntegerField()
    average = models.FloatField()
    result  = models.BooleanField()



