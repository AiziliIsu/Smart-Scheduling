from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .models import User, Profile, Course, Professor, Classroom
from .serializers import UserSerializer, ProfileSerializer, CourseSerializer, ProfessorSerializer, ClassroomSerializer

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileListView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ProfessorListView(ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class ClassroomListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

