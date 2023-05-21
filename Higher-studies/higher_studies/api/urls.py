from django.urls import path, include
from . import views
from database.models import Student


urlpatterns = [
    path('students/', views.getStudents),
    path('courses/', views.getCourses),
    path('enrollments/', views.getEnrollments),
    path('Students/<int:object_id>/', views.get_object, name='get-object'),
]
