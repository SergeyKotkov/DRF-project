from django.db import models

from config.settings import AUTH_USER_MODEL


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    preview = models.ImageField(upload_to="course_previews/", verbose_name="Превью", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец курса", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

class Lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    preview = models.ImageField(upload_to="lesson_previews/", blank=True, null=True, verbose_name="Превью")
    video_link = models.URLField(verbose_name="Ссылка на видео")
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="lessons", verbose_name="Курс",
        default=1
    )
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец курса", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

class Subscription(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', blank=True, null=True)
    sign_of_subscription = models.BooleanField(default=False, verbose_name='Признак подписки')

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

    def __str__(self):
        return f'{self.user}: {self.course}'
