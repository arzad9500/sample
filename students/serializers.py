from rest_framework.serializers import ModelSerializer
from students.models import *


class Student_serializer(ModelSerializer):
    class Meta :
        model = Student
        fields = '__all__'


class  Task_serializers(ModelSerializer):

    class Meta :

        model  = Task
        fields = '__all__'

class Student_task_serializer(ModelSerializer):
    all_task = Task_serializers(many=True)      # this for a student has many task

    class Meta :
        model = Student
        fields = '__all__'

# check video 18
class  Task_data_serializers(ModelSerializer): # see get method in taskAPI in views.py , it use this serializer (for get ) 

    student_reference = Student_serializer() # student_reference this is already in model field(foreign key field)
                                            # is in up , these for need to show students fiels insie task model(foreign key model)
    class Meta :

        model  = Task
        fields = '__all__'

class Ranksheet_serializer(ModelSerializer):

    class Meta :
        model = Ranksheet
        fields ='__all__'