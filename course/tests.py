from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Lesson, Course, Subscription
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test3@test3.ru')
        self.course = Course.objects.create(name='Введение', description='знакомство', owner=self.user)
        self.lesson = Lesson.objects.create(name='Введение', description='знакомство', course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_course_retrieve(self):
        url = reverse('course:course-detail', args=(self.course.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.course.name
        )

    def test_course_create(self):
        url = reverse('course:course-list')
        data = {
            'name': 'Python',
            'description': 'Знакомство с python'
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Course.objects.all().count(), 2
        )

    def test_course_update(self):
        url = reverse('course:course-detail', args=(self.course.pk,))
        data = {
            'name': 'Python2'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), 'Python2'
        )

    def test_course_delete(self):
        url = reverse('course:course-detail', args=(self.course.pk,))

        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Course.objects.all().count(), 0
        )

    def test_course_list(self):
        def test_course_list(self):
            url = reverse('course:course-list')
            response = self.client.get(url)
            data = response.json()

            self.assertEqual(
                response.status_code, status.HTTP_200_OK
            )
            self.assertIn('count', data)
            self.assertIn('next', data)
            self.assertIn('previous', data)
            self.assertIn('results', data)
            self.assertEqual(data['count'], 1)
            self.assertEqual(data['next'], None)
            self.assertEqual(data['previous'], None)
            self.assertEqual(len(data['results']), 1)
            self.assertEqual(data['results'][0]['name'], 'Введение')
            self.assertEqual(data['results'][0]['description'], 'знакомство')
            self.assertEqual(data['results'][0]['owner'], self.user.id)
class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test3@test3.ru')
        self.course = Course.objects.create(name='Python/git', description='Введение в git.hub', owner=self.user)
        self.lesson = Lesson.objects.create(name='Git', description='Знакомство с git', course=self.course,
                                            owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('course:lesson_retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse('course:lesson_create')
        data = {
            'name': 'Python',
            'description': 'Знакомство с python',
            'video_link': 'https://www.youtube.com/watch?v=jV9uXh_1Pso',
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse('course:lesson_update', args=(self.lesson.pk,))
        data = {
            'name': 'Python2'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), 'Python2'
        )

    def test_lesson_delete(self):
        url = reverse('course:lesson_delete', args=(self.lesson.pk,))

        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )

    def test_lesson_list(self):
        url = reverse('course:lesson_list')
        response = self.client.get(url)
        # print(response.json())
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "name": self.lesson.name,
                    "description": self.lesson.description,
                    "lesson_preview": None,
                    "url_video": None,
                    "course": self.course.pk,
                    "owner": self.user.pk
                }]}
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        # self.assertEqual(
        #   data, result
    # )


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test3@test3.ru')
        self.course = Course.objects.create(name='Python/git', description='Введение в git.hub', owner=self.user)
        self.lesson = Lesson.objects.create(name='Git', description='Знакомство с git', course=self.course,
                                            owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_subscription_create(self):
        url = reverse('course:course_subscription')
        data = {
            'user': 6,
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, {'message': 'подписка добавлена'}
        )

    def test_subscription_delete(self):
        self.subscription = Subscription.objects.create(user=self.user, course=self.course)
        url = reverse('course:course_subscription')
        data = {
            'user': self.user.pk,
            'course': self.course.pk
        }
        response = self.client.post(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data, {'message': 'подписка удалена'}
        )
