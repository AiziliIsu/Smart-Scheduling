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
    course = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        write_only = True
    )
    
    course_data = CourseSerializer(source='course', read_only=True)
    
    def create(self, validated_data):
        course_data = validated_data.pop('course', None)
        if isinstance(course_data, dict):
            course, _ = Course.objects.get_or_create(**course_data)
        else:
            course = course_data
        return Lesson.objects.create(course = course, **validated_data)
    
    class Meta:
        model = Lesson
        fields = '__all__'


class TimeSlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlots
        fields = "__all__"