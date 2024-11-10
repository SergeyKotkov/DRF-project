from django.contrib import admin
from course.models import Course, Lesson, Subscription


@admin.register(Course)
class Course(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'description')

@admin.register(Lesson)
class Lesson(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'description')

@admin.register(Subscription)
class Subscription(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('name', 'description')