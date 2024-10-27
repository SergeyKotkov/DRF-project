from rest_framework.serializers import ModelSerializer, SerializerMethodField
from course.models import Course, Lesson

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

class CourseDetailSerializer(ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    lesson_count = SerializerMethodField()

    def get_lesson_count(self, course):
        return Lesson.objects.filter(course=course).count()

    class Meta:
        model = Course
        fields = ("name", "description", "preview", "lessons", "lesson_count")