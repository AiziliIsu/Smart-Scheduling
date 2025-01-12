from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Course, Individual, Lesson, TimeSlots
from .serializers import CourseSerializer, IndividualSerializer, LessonSerializer, TimeSlotsSerializer


class CourseListCreateView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class IndividualListCreateView(ListCreateAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer


class IndividualRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer


class LessonListCreateView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class TimeSlotsListCreateView(ListCreateAPIView):
    queryset = TimeSlots.objects.all()
    serializer_class = TimeSlotsSerializer


class TimeSlotsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = TimeSlots.objects.all()
    serializer_class = TimeSlotsSerializer
