from django.urls import path
from .views import (
    CourseListCreateView, CourseRetrieveUpdateDestroyView,
    IndividualListCreateView, IndividualRetrieveUpdateDestroyView,
    LessonListCreateView, LessonRetrieveUpdateDestroyView,
    TimeSlotsListCreateView, TimeSlotsRetrieveUpdateDestroyView
)

urlpatterns = [
    # Course URLs
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyView.as_view(), name='course-detail'),

    # Individual URLs
    path('individuals/', IndividualListCreateView.as_view(), name='individual-list-create'),
    path('individuals/<int:pk>/', IndividualRetrieveUpdateDestroyView.as_view(), name='individual-detail'),

    # Lesson URLs
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyView.as_view(), name='lesson-detail'),

    # TimeSlots URLs
    path('timeslots/', TimeSlotsListCreateView.as_view(), name='timeslot-list-create'),
    path('timeslots/<int:pk>/', TimeSlotsRetrieveUpdateDestroyView.as_view(), name='timeslot-detail'),
]




