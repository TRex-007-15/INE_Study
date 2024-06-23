from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, LogoutView, CourseDetailView, LessonDetailView, EnrollView, CourseListView, CourseUpdateDeleteView, LessonListView, LessonUpdateDeleteView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='auth_login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('courses/<int:pk>/update/', CourseUpdateDeleteView.as_view(), name='course_update_delete'),
    path('courses/<int:courseId>/lessons/', LessonListView.as_view(), name='lesson_list'),
    path('courses/<int:courseId>/lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
    path('courses/<int:courseId>/lessons/<int:lessonId>/update/', LessonUpdateDeleteView.as_view(), name='lesson_update_delete'),
    path('enrollments/', EnrollView.as_view(), name='enroll'),
]
