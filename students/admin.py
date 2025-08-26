from django.contrib import admin
from students import models
###### from .models import student  # when we use this do like 6th line

# Register your models here.
######admin.site.register(Student) # 

admin.site.register(models.Student)

admin.site.register(models.Ranksheet)