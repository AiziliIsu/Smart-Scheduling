from rest_framework import serializers
from .models import Individual, Course, Lesson, Classroom
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class IndividualSerializer(serializers.ModelSerializer):
    courses_as_student = CourseSerializer(many=True)  # Many-to-many relationship with Course
    courses_as_teacher = CourseSerializer(many=True)  # Many-to-many relationship with Course
    class Meta:
        model = Individual
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer()  # Nested CourseSerializer for detailed info
    class Meta:
        model = Lesson
        fields = '__all__'


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'


# class ScheduleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Schedule
#         fields = ['id', 'course', 'professor', 'classroom', 'day_of_week', 'start_time', 'end_time']


