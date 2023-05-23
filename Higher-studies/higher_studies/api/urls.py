from django.urls import path, include
from . import views
from database.models import Student
from .views import course_names, student_details_with_course ,getCoursesOnly
from .views import update_student
from .views import StudentDeleteView

urlpatterns = [
    path('students/', views.getStudents),
    path('courses/', views.getCourses),
    path('enrollments/', views.getEnrollments),
    path('Students/<int:student_id>/', student_details_with_course, name='student-details'),
    path('Students/addNewStudent/', views.add_student, name='add_student'),#used in adding new student from form
    path('Courses/', course_names, name='course-names'),
    path('api/update-student/<int:pk>/', update_student, name='update-student'),
    path('CoursesOnly/', getCoursesOnly, name='get-courses'),
    path('delete-student/', views.delete_student, name='delete-student'),
    path('delete-with-pk/<int:pk>/', StudentDeleteView.as_view(), name='delete-with-pk'),
]