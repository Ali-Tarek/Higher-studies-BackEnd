from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from database.models import Student, Course, Enrollment
from .serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer , StudentUpdateSerializer,CourseSerializerOnly
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json








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
def getCoursesOnly(request):
    courses = Course.objects.all()
    serializer = CourseSerializerOnly(courses, many=True)
    return Response({'courses': serializer.data})

@api_view(['GET'])
def getEnrollments(request):
    Enrollments = Enrollment.objects.all()
    serializer = EnrollmentSerializer(Enrollments, many=True)
    return Response(serializer.data)


"""
@api_view(['GET'])
def get_object(request, object_id):
    # Retrieve the object from the database using the provided ID
    your_object = get_object_or_404(Student, id=object_id)

    # Serialize the object
    serializer = StudentSerializer(your_object)

    # Return the serialized object as a response
    return Response(serializer.data)

"""
@api_view(['GET'])
def student_details_with_course(request, student_id):
    try:
        student = Student.objects.select_related('course1', 'course2', 'course3').get(id=student_id)
        courses = [student.course1, student.course2, student.course3]
        course_data = []
        for course in courses:
            if course:
                course_data.append({
                    'id': course.id,
                    'name': course.name,
                    'department': course.department,
                    'day': course.day,
                    'hours': course.hours,
                    'hallnumber': course.hallnumber,
                })
        
        student_data = {
            'id': student.id,
            'firstName': student.firstName,
            'lastName': student.lastName,
            'gender': student.gender,
            'status': student.status,
            'dob': student.dob,
            'university': student.university,
            'department': student.department,
            'courses': course_data,
        }
        return Response(student_data)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def course_names(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    course_names = [course['name'] for course in serializer.data]
    return Response(course_names)


@api_view(['POST'])
def update_student(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'message': 'Student not found'}, status=404)
    
    # Retrieve the JSON data from the request
    data = request.data
    
    # Update the student fields based on the received data
    student.firstName = data.get('firstName', student.firstName)
    student.lastName = data.get('lastName', student.lastName)
    student.gender = data.get('gender', student.gender)
    student.status = data.get('status', student.status)
    student.dob = data.get('dob', student.dob)
    student.university = data.get('university', student.university)
    course1_id = data.get('course1', None)
    course2_id = data.get('course2', None)
    course3_id = data.get('course3', None)
    student.department = data.get('department', student.department)
    if course1_id is not None:
        student.course1_id = course1_id

    if course2_id is not None:
        student.course2_id = course2_id

    if course3_id is not None:
        student.course3_id = course3_id

    
    student.save()
    
    return Response({'message': 'Student updated successfully'})


@api_view(['POST'])
@csrf_exempt
def delete_student(request):
    # Retrieve the student ID from the request data
    student_id = request.data.get('student_id')

    if student_id:
        try:
            student = Student.objects.get(id=student_id)
            student.delete()
            return Response({'message': 'Student deleted successfully'})
        except Student.DoesNotExist:
            return Response({'message': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
    

