from django.urls import path, include
from . import views
from database.models import Student


urlpatterns = [
    path('students/', views.getStudents),# used in Backend validation to sure that the user did not enter duplicated ID
    path('courses/', views.getCourses, name='getCourses'),#used in  rendering courses to the form
    path('enrollments/', views.getEnrollments),
    path('Students/<int:object_id>/', views.get_object, name='get-object'),
    path('Students/addNewStudent/', views.add_student, name='add_student'),#used in adding new student from form
]
