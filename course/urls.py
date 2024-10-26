from django.urls import path
from rest_framework.routers import SimpleRouter

from course.views import CourseViewSet, LessonCreatAPIView, LessonListAPIView, LessonUpdateAPIView, LessonRetrieveAPIView, LessonDestroyAPIView
from course.apps import CourseConfig

app_name = CourseConfig.name

router = SimpleRouter()
router.register(r"course", CourseViewSet)

urlpatterns = [
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lesson/create/', LessonCreatAPIView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),

]

urlpatterns += router.urls
