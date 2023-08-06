from django import forms
from .models import *


class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = '__all__'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
