from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from database.models import Student, Course, Enrollment
from .serializers import StudentSerializer, CourseSerializer, EnrollmentSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
@api_view(['POST'])
def add_student(request):
    if request.method == 'POST':
        data = request.data
       
        if data['Gender'] == 'Male':
            data["Gender"] = 'M'
        else:
            data["Gender"] = 'F'
        if data['Active'] == 'Active':
            data["Active"] = 'A'
        else:
            data["Active"] = 'I'
        data['Date'] = data['Date'].replace("/", "-")
        
        serializer = StudentSerializer(data={
            'id':data['ID'],
            'firstName': data['fname'],
            'lastName': data['lname'],
            'gender': data['Gender'],
            'status': data['Active'],
            'dob': data['Date'],
            'university': data['Uni'],
            'course1': data['course_1'],
            'course2': data['course_2'],
            'course3': data['course_3'],
            'department': data['Dept']
        })
       
        if serializer.is_valid():
            student = serializer.save()
        else:
            response_data = {'error': 'ID is aleady Existed'}
            return JsonResponse(response_data, status=400)
        
        Response_Data = {'message': "Student added successfully"}
        return JsonResponse(Response_Data)
 

@api_view(['GET'])
def getCourses(request):
    courses = Course.objects.all()  # Retrieve all Course objects

    serializer = CourseSerializer(courses, many=True)  # Set many=True to serialize multiple objects

    return Response(serializer.data)








