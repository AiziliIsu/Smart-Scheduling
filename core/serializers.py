from rest_framework import serializers
from .models import Individual, Course, Lesson, TimeSlots
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
    courses_as_student = CourseSerializer(many=True)
    courses_as_teacher = CourseSerializer(many=True)
    class Meta:
        model = Individual
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = Lesson
        fields = '__all__'


class TimeSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlots
        fields = "__all__"