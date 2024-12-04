from django.urls import path

from .views import (
    UserListView,
    LessonViewSet,
    IndividualListView,
    ProfessorListView,
    StudentListView,
    CourseListView,
    ClassroomListView,
    ScheduleListView,
    LessonListView,  # New view to list lessons
    CourseLessonListView,  # View for listing lessons for a specific course
)



urlpatterns = [
    path('users/', UserListView.as_view(), name='users'),
    path('individuals/', IndividualListView.as_view(), name='individuals'),
    path('professors/', ProfessorListView.as_view(), name='professors'),
    path('students/', StudentListView.as_view(), name='students'),
    path('courses/', CourseListView.as_view(), name='courses'),
    path('classrooms/', ClassroomListView.as_view(), name='classrooms'),
    path('schedules/', ScheduleListView.as_view(), name='schedules'),
    
    # New routes for Lesson
    path('lessons/', LessonListView.as_view(), name='lessons'),  # List all lessons
    path('courses/<int:course_id>/lessons/', CourseLessonListView.as_view(), name='course_lessons'),  # List lessons for a specific course
]




