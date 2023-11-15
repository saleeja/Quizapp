# models.py

from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    options = models.JSONField()
    correct_answer = models.CharField(max_length=255)

class Test(models.Model):
    questions = models.ManyToManyField(Question)
    allowed_time = models.IntegerField()

class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    answered_questions = models.ManyToManyField(Question)
    scores = models.JSONField(default=dict)
