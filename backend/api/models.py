import json
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_admin = models.BooleanField(default=False)

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    syllabus = models.TextField(default='[]')  # Store syllabus as JSON in a TextField
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    type = models.TextField(default="Python")

    def set_syllabus(self, syllabus):
        self.syllabus = json.dumps(syllabus)

    def get_syllabus(self):
        return json.loads(self.syllabus)

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video_url = models.URLField(default="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    text_material = models.TextField()
    order = models.PositiveIntegerField()

class Content(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='contents', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
