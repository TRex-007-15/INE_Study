# views.py

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, Course, Enrollment, Lesson, Content, Instructor
from .serializers import UserSerializer, CourseSerializer, EnrollmentSerializer, LessonSerializer, ContentSerializer, InstructorSerializer
from .permissions import IsAdminUserOrReadOnly, IsEnrolledOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Lesson, Course
from .serializers import LessonSerializer
from .permissions import IsEnrolledOrReadOnly
from django.shortcuts import get_object_or_404
# Authentication Views
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            token = RefreshToken(request.data.get('refresh'))
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# Course Detail View
class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Lesson Detail View
class LessonDetailView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsEnrolledOrReadOnly]

# Enrollment View
class EnrollView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        course_id = request.data.get('course_id')
        course = Course.objects.get(id=course_id)
        enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)
        if created:
            return Response({"message": "Enrolled successfully."}, status=status.HTTP_201_CREATED)
        return Response({"message": "Already enrolled."}, status=status.HTTP_200_OK)

# List Courses and Create Course
class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        instructor_data = self.request.data.get('instructor')
        instructor = Instructor.objects.get(pk=instructor_data['id'])
        serializer.save(instructor=instructor)

# Retrieve, Update, Destroy Course
class CourseUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUserOrReadOnly]

# List Lessons and Create Lesson
class LessonListView(generics.ListCreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsEnrolledOrReadOnly]

    def get_queryset(self):
        course_id = self.kwargs['course_id']  # Corrected to 'course_id'
        course = get_object_or_404(Course, id=course_id)
        return Lesson.objects.filter(course=course)

    def perform_create(self, serializer):
        course_id = self.kwargs['course_id']  # Corrected to 'course_id'
        course = get_object_or_404(Course, id=course_id)
        serializer.save(course=course)

# Retrieve, Update, Destroy Lesson
class LessonUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsEnrolledOrReadOnly]

    def get_queryset(self):
        course_id = self.kwargs['courseId']
        lesson_id = self.kwargs['lessonId']
        return Lesson.objects.filter(course__id=course_id, id=lesson_id)
