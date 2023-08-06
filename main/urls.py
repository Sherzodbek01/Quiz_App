from django.urls import path, include
from .views import *


urlpatterns = [
    path('create-direction/', create_direction),
    path('all-direction/', all_direction),
    path('directions/<int:pk>/', direction_detail, name='direction'),
    path('directions/update/<int:pk>/', update_direction, name='update-direction'),
    path('directions/delete/<int:pk>/', delete_direction, name='delete-direction'),
    path('backoffice/', include('main.backoffice.urls')),
    path('create_register/', create_register),
    path('get_direction/', get_direction),
    path('get_question/', get_question),
    path('create-question/', create_question),
    path('all-question/', all_question),
    path('questions/update/<int:pk>/', update_question, name='update-question'),
    path('questions/delete/<int:pk>/', delete_question, name='delete-question'),
    path('create_answer/', create_answer),
]