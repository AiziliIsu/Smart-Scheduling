from django.urls import path
from .views import UserListView, ProfileListView, CourseListView, ProfessorListView, ClassroomListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('profiles/', ProfileListView.as_view(), name='profile-list'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('professors/', ProfessorListView.as_view(), name='professor-list'),
    path('classrooms/', ClassroomListView.as_view(), name='classroom-list'),
]
