from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from database.models import Student, Course, Enrollment
from .serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse


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



@api_view(['GET'])
def get_object(request, object_id):
    # Retrieve the object from the database using the provided ID
    your_object = get_object_or_404(Student, id=object_id)

    # Serialize the object
    serializer = StudentSerializer(your_object)

    # Return the serialized object as a response
    return Response(serializer.data)

