from django.urls import path
from . views import *

from rest_framework_simplejwt.views import ( # for jwt token
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('user/', userview.as_view()),
    path('login/', user_login_view.as_view()),

    # this for jwt token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
