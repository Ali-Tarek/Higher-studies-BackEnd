from django.urls import path, include
from . import views

urlpatterns = [
    path('students/', views.getStudents),
    path('courses/', views.getCourses),
    path('enrollments/', views.getEnrollments),
]
