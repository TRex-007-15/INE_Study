# serializers.py

from rest_framework import serializers
from .models import User, Course, Enrollment, Lesson, Content, Instructor

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class InstructorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Instructor
        fields = ['id', 'user', 'bio']

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video_url', 'text_material', 'order']

class CourseSerializer(serializers.ModelSerializer):
    instructor = serializers.PrimaryKeyRelatedField(queryset=Instructor.objects.all())
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'syllabus', 'instructor', 'lessons','type']

    def create(self, validated_data):
        instructor_data = validated_data.pop('instructor')
        instructor = Instructor.objects.get(pk=instructor_data['id'])

        course = Course.objects.create(
            instructor=instructor,
            **validated_data
        )
        return course

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.syllabus = validated_data.get('syllabus', instance.syllabus)
        
        instructor_data = validated_data.get('instructor', None)
        if instructor_data:
            instructor = Instructor.objects.get(pk=instructor_data['id'])
            instance.instructor = instructor
        
        instance.save()
        return instance

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course']

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'lesson', 'title', 'body']
