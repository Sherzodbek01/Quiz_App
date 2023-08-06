from django.urls import path
from .views import *


urlpatterns = [
    path('', index_view, name='index'),
    path('registered/users/', registered_users_view, name='registered-users'),
    path('direction/', direction_view, name='direction'),
    path('question/', question_view, name='question'),
    path('user/result', user_result, name='user-result'),
]