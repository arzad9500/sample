from django.urls import path
from students.views import *  # StudentAPI is class 

urlpatterns = [
    path('details/',StudentAPI.as_view()), # this for get and post
    path('details/<int:student_id>/',StudentAPI.as_view()),

    path('task/',TaskAPI.as_view()),
    path('task/<int:task_id>/',TaskAPI.as_view()),
    path('rank/',RanksheetAPI.as_view()),
    path('rank/<int:student_id>/',RanksheetAPI.as_view()),
    
    path('task/list/create/',task_list_create),
    path('task/update/delete/<int:id>/',task_update_delete)

    # path('task//',TaskAPIById.as_view()),
    
    


]