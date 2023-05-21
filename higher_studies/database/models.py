from django.db import models


class Course(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    day = models.IntegerField()
    hours = models.IntegerField()
    hallnumber = models.CharField(max_length=255)

    students = models.ManyToManyField('Student', through='Enrollment')


class Student(models.Model):
    Genders = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    Status = [
        ("A", "Active"),
        ("I", "Inactive"),
    ]

    id = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=Genders)
    status = models.CharField(max_length=1, choices=Status)
    dob = models.DateField()
    university = models.CharField(max_length=255)
    course1 = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='students_course1')
    course2 = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='students_course2')
    course3 = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='students_course3')
    department = models.CharField(max_length=255)


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # additional fields related to enrollment, such as grade, enrollment date, etc.
