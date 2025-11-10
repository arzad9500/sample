from django.urls import path,include # this include for (viewset in views and router)
# from .router import liberaty_router # 
from liberary import router 
from .views import *

urlpatterns = [
    path('api/',include(router.liberary_router.urls)), # check above 2 line 
    path('laptop/',laptopView.as_view()), # here we use generics
    path('laptop/<int:pk>/',laptopViewById.as_view()), # pk(primary key) is default(mandatory keyword) for generics


]