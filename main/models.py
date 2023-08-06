from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Register(models.Model):
    ful_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.ful_name}, {self.phone}"


class Direction(models.Model):
    type = models.CharField(max_length=255)
    is_logic = models.BooleanField()
    number_of_question = models.IntegerField()
    time = models.IntegerField(help_text="duration of  the quiz in minutes")
    score = models.IntegerField(help_text="score to be awarded")

    def __str__(self):
        return self.type


class Content(models.Model):
    questiona = RichTextUploadingField()
    questionb = RichTextUploadingField()
    questionc = RichTextUploadingField()
    questiond = RichTextUploadingField()
    correct = models.CharField(choices=(
        ("a", "a"),
        ("b", "b"),
        ("c", "c"),
        ("d", "d"),
    ), max_length=1)


class Question(models.Model):
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answera = models.CharField(max_length=255)
    answerb = models.CharField(max_length=255)
    answerc = models.CharField(max_length=255)
    answerd = models.CharField(max_length=255)
    correct = models.CharField(choices=(
        ("a", "a"),
        ("b", "b"),
        ("c", "c"),
        ("d", "d"),
    ), max_length=1)
    question_photo = models.ManyToManyField(Content, null=True, blank=True)

    def __str__(self):
        return self.question


class UserResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    correct = models.IntegerField()
    total = models.IntegerField(help_text="Enter the number of correct options")
    percentage = models.FloatField(help_text="Enter the result as a percentage")
    incorrect = models.IntegerField()


class UQA(models.Model):
    user_result = models.OneToOneField(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(UserResult, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_result


