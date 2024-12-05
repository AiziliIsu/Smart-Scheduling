from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Individual, Course,  Lesson, Classroom
from .serializers import UserSerializer, IndividualSerializer, LessonSerializer, CourseSerializer, ClassroomSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LessonListView(APIView):
    """
    View to list all lessons
    """
    def get(self, request, *args, **kwargs):
        lessons = Lesson.objects.all()
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

class CourseLessonListView(APIView):
    """
    View to list lessons for a specific course
    """
    def get(self, request, course_id, *args, **kwargs):
        try:
            course = Course.objects.get(id=course_id)
            lessons = course.lessons.all()
            serializer = LessonSerializer(lessons, many=True)
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)


class LessonViewSet(viewsets.ModelViewSet):
     queryset = Lesson.objects.all()
     serializer_class = LessonSerializer

class CourseListView(ListAPIView):
    """
    List all courses.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class IndividualListView(ListAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer


class ProfessorListView(ListAPIView):
    """
    List all individuals with the role of 'professor'.
    """
    queryset = Individual.objects.filter(role='professor')
    serializer_class = IndividualSerializer


class StudentListView(ListAPIView):
    """
    List all individuals with the role of 'student'.
    """
    queryset = Individual.objects.filter(role='student')
    serializer_class = IndividualSerializer





class ClassroomListView(ListAPIView):
    """
    List all classrooms.
    """
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


# class ScheduleListView(ListAPIView):
#     """
#     List all schedules.
#     """
#     queryset = Schedule.objects.all()
#     serializer_class = ScheduleSerializer


