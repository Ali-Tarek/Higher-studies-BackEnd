from rest_framework import serializers
from database.models import Student, Course, Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'firstName', 'lastName', 'gender', 'status', 'dob', 'university', 'course1', 'course2', 'course3', 'department']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'department', 'day', 'hours', 'hallnumber', 'students']


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']


class CourseSerializerOnly(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'department', 'day', 'hours', 'hallnumber']

class StudentUpdateSerializer(serializers.ModelSerializer):
    department = serializers.CharField(source='course1.department')

    class Meta:
        model = Student
        fields = ['firstName', 'lastName', 'gender', 'status', 'dob', 'university', 'department']

    def update(self, instance, validated_data):
        # Update the instance with the validated data
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.status = validated_data.get('status', instance.status)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.university = validated_data.get('university', instance.university)

        # Save the instance
        instance.save()

        return instance