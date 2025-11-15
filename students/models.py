from django.db import models

# Create your models here.
class Student(models.Model):
    name     = models.CharField(max_length=100)
    age      = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Task (models.Model): # Student shoud be before(up) coz foreign key
    # can be also use other model here
    student_reference = models.ForeignKey(Student,related_name='all_task', null=True, on_delete=models.CASCADE)
    task_name   = models.CharField(max_length=150)
    description = models.TextField()
    # related_name='all_task' --> this is need to see task for the student and the serializers (Student_task_serializer)


class Ranksheet(models.Model):
    tamil   = models.IntegerField()
    english = models.IntegerField()
    maths   = models.IntegerField()
    science = models.IntegerField()
    social  = models.IntegerField()
    total   = models.IntegerField()
    average = models.FloatField()
    result  = models.BooleanField()



