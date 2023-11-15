# urls.py

from django.urls import path
from .views import QuestionList, TestList, UserProgressDetail

urlpatterns = [
    path('questions/', QuestionList.as_view(), name='question-list'),
    path('tests/', TestList.as_view(), name='test-list'),
    path('user-progress/', UserProgressDetail.as_view(), name='user-progress-detail'),
]
