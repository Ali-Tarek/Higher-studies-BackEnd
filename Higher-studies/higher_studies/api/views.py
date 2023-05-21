from rest_framework.response import Response
from rest_framework.decorators import api_view
from database.models import Student, Course, Enrollment
from .serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer


@api_view(['GET'])
def getStudents(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getCourses(request):
    Courses = Course.objects.all()
    serializer = CourseSerializer(Courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getEnrollments(request):
    Enrollments = Enrollment.objects.all()
    serializer = EnrollmentSerializer(Enrollments, many=True)
    return Response(serializer.data)
