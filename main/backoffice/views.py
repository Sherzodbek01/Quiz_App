from django.shortcuts import render


def index_view(request):
    return render(request, 'dashboard-ecommerce.html')


def registered_users_view(request):
    return render(request, 'registered-users.html')


def direction_view(request):
    return render(request, 'directions.html')


def question_view(request):
    return render(request, 'question.html')


def user_result(request):
    return render(request, 'user-result.html')
