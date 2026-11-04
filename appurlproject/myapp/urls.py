from django.urls import path
from .views import view1

urlpatterns = [
    path('my/', view1),
]