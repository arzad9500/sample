from rest_framework.routers import DefaultRouter
from .views import BookView

liberary_router = DefaultRouter()
liberary_router.register(r'book',BookView)