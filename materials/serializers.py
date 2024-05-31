from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from materials.models import Course, Lesson
from materials.validators import validate_link


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = SerializerMethodField()
    info_lessons = SerializerMethodField()

    def get_count_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_info_lessons(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    link = serializers.CharField(validators=[validate_link])

    class Meta:
        model = Lesson
        fields = '__all__'
