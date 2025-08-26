from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from students.serializers import *

from rest_framework.decorators import api_view


class  StudentAPI(APIView): # inherit with apiview so it is api class

    def get(self,request): #1

        all_student=Student.objects.all() #2 # Student is model

        student_data =  Student_task_serializer(all_student,many= True).data

        # student_list =[]     #6

        # for s in all_student: #4
        #     student_dict = {  #5
        #         "id"   :s.id,
        #         "name" : s.name,
        #         "age"  : s.age
        #         }
            
        #     student_list.append(student_dict) #7

        return Response(student_data) # 


    def post(self,request):

        # print(request.data) # data is container(keywoard) it will save the frontend post data # this will print in terminal
        
        new_student=Student(name=request.data['name'],age=request.data['age'])# first name is from Studens (models) key name , 2nd name is from frontend
        new_student.save()

        return Response('new student added')
    
    def patch(self,request,student_id): # this need seperate url because this has 3 parameter
        
        # print(student_id,' rd student_id')

        student_data = Student.objects.filter(id = student_id)

        # print(student_data)
        # print(request.data)
        student_data.update(name=request.data['name'],age=request.data['age'])

        return Response('data updated')
    
    def delete(self, requuest , student_id):

        student_data = Student.objects.get(id = student_id)
        student_data.delete()

        return Response ('student id deleted')

class TaskAPI(APIView):

    def get(self, request , task_id = None):

        if task_id == None :

            all_task = Task.objects.all()
            task_data =  Task_data_serializers(all_task,many = True).data
            
            return Response (task_data)
        
        else :

            task = Task.objects.get(id = task_id)

            task_data =  Task_data_serializers(task,).data

            return Response (task_data)

    def post(self, request):

        new_task = Task_serializers(data = request.data)

        if new_task.is_valid():
            new_task.save()
            return Response ('new task added')
        
        else:
            return Response (new_task.errors)
    
    def patch (self , request , task_id):

        task = Task.objects.get(id = task_id)

        update_task = Task_serializers(task , data =request.data,  partial =True )

        if update_task.is_valid() :

            update_task.save()

            return Response ('task was updated')
        
        else :
            return Response (update_task.errors)
        
    def put (self , request , task_id):

        task = Task.objects.get(id = task_id)

        update_task = Task_serializers(task , data =request.data,  partial =True )

        if update_task.is_valid() :

            update_task.save()

            return Response ('task was updated')
        
        else :
            return Response (update_task.errors)
        
    def delete(self, request , task_id):

        task = Task.objects.get(id = task_id)

        task.delete()

        return Response ('task deleted')


class RanksheetAPI(APIView):

    def get(self, request , student_id = None):

        if student_id == None :

            all_student = Ranksheet.objects.all()
            data = Ranksheet_serializer(all_student,many = True).data
            
            return Response (data)
        
        else :

            student = Ranksheet.objects.get(id = student_id)

            data = Ranksheet_serializer(student).data

            return Response (data)

    def post(self, request):

        total_mark = (request.data['tamil'] + request.data['english']
        + request.data['maths'] + request.data['science'] + request.data['social'])

        average_mark = total_mark / 5

        if (request.data['tamil'] >=35) and  (request.data['english'] >=35) and (request.data['maths'] >=35) and (request.data['science'] >=35) and (request.data['social'] >=35) :
            student_result = True
        else :
            student_result = False


        new_data = Ranksheet(tamil =request.data['tamil'],english =request.data['english'],
                maths =request.data['maths'],science =request.data['science'],social =request.data['social'],
                total = total_mark,average  =  average_mark,result = student_result )
        
        new_data.save()

        return Response ('student mark saved')
    
    def patch(self , request , student_id):

        rank_data = Ranksheet.objects.filter(id = student_id)

        total_mark = (request.data['tamil'] + request.data['english']
        + request.data['maths'] + request.data['science'] + request.data['social'])

        average_mark = total_mark / 5

        if (request.data['tamil'] >=35) and  (request.data['english'] >=35) and (request.data['maths'] >=35) and (request.data['science'] >=35) and (request.data['social'] >=35) :
            student_result = True
        else :
            student_result = False


        rank_data.update(tamil =request.data['tamil'],english =request.data['english'],
                maths =request.data['maths'],science =request.data['science'],social =request.data['social'],
                total = total_mark,average  =  average_mark,result = student_result )
        
        return Response ('student data patch method updated')
    
    def put(self , request , student_id):

        rank_data = Ranksheet.objects.filter(id = student_id)

        total_mark = (request.data['tamil'] + request.data['english']
        + request.data['maths'] + request.data['science'] + request.data['social'])

        average_mark = total_mark / 5

        if (request.data['tamil'] >=35) and  (request.data['english'] >=35) and (request.data['maths'] >=35) and (request.data['science'] >=35) and (request.data['social'] >=35) :
            student_result = True
        else :
            student_result = False


        rank_data.update(tamil =request.data['tamil'],english =request.data['english'],
                maths =request.data['maths'],science =request.data['science'],social =request.data['social'],
                total = total_mark,average  =  average_mark,result = student_result )
        
        return Response ('student data put method updated')
    
    def delete (self , request , student_id):

        rank = Ranksheet.objects.get(id = student_id)

        rank.delete()

        return Response ('selected student data was deleted')

        
@api_view(["GET","POST"])
def task_list_create(request):
    
    if request.method == "GET":
        
        all_task = Task.objects.all()
        task_data =  Task_serializers(all_task,many = True).data
            
        return Response (task_data)
        
    elif request.method == "POST" :
        
        new_task = Task_serializers(data = request.data)

        if new_task.is_valid():
            new_task.save()
            return Response ('new task added')
        
        else:
            return Response (new_task.errors)
        
@api_view(["GET","PUT","PATCH","DELETE"])
def task_update_delete(request,id):
    
    task = Task.objects.get(id = id)
    
    if request.method == "GET":
        
        task_data =  Task_serializers(task,).data
        return Response (task_data)
    
    elif request.method == "PATCH":
        
        update_task = Task_serializers(task , data =request.data,  partial =True )

        if update_task.is_valid() :

            update_task.save()

            return Response ('task was updated')
        
        else :
            return Response (update_task.errors)
        
    elif request.method == "PUT":
        
        update_task = Task_serializers(task , data =request.data,  partial =True )

        if update_task.is_valid() :

            update_task.save()

            return Response ('task was updated')
        
        else :
            return Response (update_task.errors)
        
    elif request.method == "DELETE":
        
        task.delete()

        return Response ('task deleted')
        

        

       

