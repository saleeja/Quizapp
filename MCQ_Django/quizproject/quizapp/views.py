# views.py

from rest_framework import generics, permissions
from .models import Question, Test, UserProgress
from .serializers import QuestionSerializer, TestSerializer, UserProgressSerializer

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class TestList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class UserProgressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProgress.objects.all()
    serializer_class = UserProgressSerializer
    permission_classes = [permissions.IsAuthenticated]
