from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('quizapp.urls')),
    path('api/admin/', admin.site.urls),
]

