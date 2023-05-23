from django.urls import path, include
from . import views
from database.models import Student
from .views import course_names, student_details_with_course ,getCoursesOnly
from .views import update_student

urlpatterns = [
    path('students/', views.getStudents),
    path('courses/', views.getCourses),
    path('enrollments/', views.getEnrollments),
    path('Students/<int:student_id>/', student_details_with_course, name='student-details'),
    path('Courses/', course_names, name='course-names'),
    path('api/update-student/<int:pk>/', update_student, name='update-student'),
    path('CoursesOnly/', getCoursesOnly, name='get-courses'),
    path('delete-student/', views.delete_student, name='delete-student'),
]