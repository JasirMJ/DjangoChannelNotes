from django.urls import path
from .views import *

urlpatterns = [
    path('',NoteList.as_view()),
    path('<int:pk>/',NoteDetails.as_view()), #api/v1/Notes/1
]

