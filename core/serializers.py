from rest_framework import serializers
from .models import Individual, Course, Lesson, Classroom, Schedule
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'code', 'description', 'duration', 'is_mandatory', 'scaler_value']

class IndividualSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)  # Many-to-many relationship with Course
    class Meta:
        model = Individual
        fields = ['id', 'name', 'email', 'role', 'courses', 'scaler_value']


class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer()  # Nested CourseSerializer for detailed info
    class Meta:
        model = Lesson
        fields = ['id', 'course', 'lesson_type', 'times_per_week', 'courses']


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'name', 'capacity']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'course', 'professor', 'classroom', 'day_of_week', 'start_time', 'end_time']


