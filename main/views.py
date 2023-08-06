import random
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from random import randint
from .serializers import *
from .forms import *
from django.http import HttpResponse
from .models import *


@api_view(['POST'])
def create_register(request):
    ful_name = request.POST.get("full_name")
    phone = request.POST.get("phone")
    register = Register.objects.create(
        ful_name=ful_name,
        phone=phone,
    )
    return Response(RegisterSerializer(register).data)


@api_view(['GET'])
def get_direction(request):
    return Response(DirectionSerializer(Direction.objects.all(), many=True).data)


def create_direction(request):
    form = DirectionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse("The information is stored in the database")
    context = {
        'form': form
    }
    return render(request, 'base.html', context)


def all_direction(request):
    direction = Direction.objects.all()
    context = {
        'direction': direction
    }
    return render(request, 'directions.html', context)


def direction_detail(request, pk):
    direction = Direction.objjects.get(id=pk)
    context = {
        'direction': direction
    }
    return render(request, 'blog.html', context)


def update_direction(request, pk):
    direction = Direction.objects.get(id=pk)
    form = DirectionForm(request.POST or None, instance=direction)
    if form.is_valid():
        form.save()
        return HttpResponse('Information has been changed')
    context = {
        'form': form
    }
    return render(request, 'update_direction.html', context)


def delete_direction(request, pk):
    direction = Direction.objects.get(id=pk)
    direction.delete()
    return redirect('all_direction')


@api_view(['GET'])
def get_question(request):
    direction_id = request.GET["direction_id"]
    if Direction.objects.filter(id=direction_id).count():
        direction = Direction.objects.get(id=direction_id)
    else:
        return Response({"success": False})
    query = Question.objects.filter(direction_id=direction_id).order_by('?')[direction.number_of_question]
    # query = list(Question.objects.filter(direction_id=direction_id))
    query = random.choices(query, k=direction.number_of_question)
    return Response(QuestionSerializer(query, many=True).data)


def create_question(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse("The information is stored in the database")

    context = {
        'form': form
    }
    return render(request, 'create_question.html', context)


def all_question(request):
    question = Question.objects.all()
    context = {
        'question': question
    }
    return render(request, 'questions.html', context)


def question_detail(request, pk):
    question = Question.objjects.get(id=pk)
    context = {
        'question': question
    }
    return render(request, 'question_detail.html', context)


def update_question(request, pk):
    question = Question.objects.get(id=pk)
    form = QuestionForm(request.POST or None, instance=question)
    if form.is_valid():
        form.save()
        return HttpResponse('Information has been changed')
    context = {
        'form': form
    }
    return render(request, 'update_question.html', context)


def delete_question(request, pk):
    question = Question.objects.get(id=pk)
    question.delete()
    return redirect('all-question')


@api_view(['GET'])
def create_answer(request):
    user_id = request.data.get("user_id")
    answers = request.data.get("answers")
    result = UserResult.objects.create(
        user=Register.objects.get(id=user_id),
        score=0,
        correct=0,
        total=0,
        incorrect=0,
        percentage=0,
    )
    score = 0
    total = 0
    correct = 0
    incorrect = 0
    for i in answers:
        q = Question.objects.get(id=i['question'])
        if q.correct == i['answer']:
            score += 10
            correct += 1
            total += 1

        else:
            incorrect += 1
    result.total = total
    result.correct = correct
    result.incorrect = incorrect
    result.percentage = (score/total) * 10

    result.save()
    return Response(
        {
            "total": total,
            "correct": correct,
            "percentage": percentage,
        }
    )

