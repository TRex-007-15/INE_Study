# admin.py
import json
from django.contrib import admin
from .models import User, Course, Enrollment, Lesson, Content, Instructor

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    pass  # Add any customizations for User admin if needed


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'course']
    list_filter = ['course']

    def save_model(self, request, obj, form, change):
        user_id = request.POST.get('user')
        course_id = request.POST.get('course')
        user = User.objects.get(pk=user_id)
        course = Course.objects.get(pk=course_id)
        obj.user = user
        obj.course = course
        obj.save()

    def delete_model(self, request, obj):
        # Perform custom delete logic here, if needed
        obj.delete()

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'course']
    search_fields = ['title', 'course__title']
    list_filter = ['course']

    def save_model(self, request, obj, form, change):
        if not change:  # If creating a new object
            course_id = request.POST.get('course')  # Assuming 'course' is sent as POST data
            course = Course.objects.get(pk=course_id)
            obj.course = course
        obj.save()

    def delete_model(self, request, obj):
        # Perform custom delete logic here, if needed
        obj.delete()

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'lesson', 'get_content_type_display']  # Assuming 'get_content_type_display' is a method
    search_fields = ['lesson__title']
    list_filter = ['lesson']

    def get_content_type_display(self, obj):
        return obj.content_type.model  # Adjust this based on how content_type is related

    get_content_type_display.short_description = 'Content Type'  # Optional: Custom header for the column

    def save_model(self, request, obj, form, change):
        if not change:  # If creating a new object
            lesson_id = request.POST.get('lesson')  # Assuming 'lesson' is sent as POST data
            lesson = Lesson.objects.get(pk=lesson_id)
            obj.lesson = lesson
        obj.save()

    def delete_model(self, request, obj):
        # Perform custom delete logic here, if needed
        obj.delete()

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    search_fields = ['user__username']
    list_filter = []


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'instructor']
    search_fields = ['title', 'instructor__username']  # Assuming instructor is User model with username field

    def save_model(self, request, obj, form, change):
        # Set the syllabus before saving the object
        syllabus_data = request.POST.get('syllabus', '[]')  # Assuming syllabus is sent as JSON string in POST data
        obj.set_syllabus(json.loads(syllabus_data))  # Convert JSON string to Python object
        super().save_model(request, obj, form, change)