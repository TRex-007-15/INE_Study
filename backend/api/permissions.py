from rest_framework import permissions
from .models import Enrollment

class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.is_admin

class IsEnrolledOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        course_id = view.kwargs.get('courseId')
        return Enrollment.objects.filter(user=request.user, course_id=course_id).exists()
