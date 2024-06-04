from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Course, Subscribe
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='admin@admin.com')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name='Python')
        self.lesson = Lesson.objects.create(name='Telegram bot')

    def test_lesson_list(self):
        url = reverse('materials:lesson-list')
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.lesson.pk,
                    "link": None,
                    "name": self.lesson.name,
                    "description": None,
                    "preview": None,
                    "course": None,
                    "owner": None
                }
            ]
        }
        self.assertEqual(
            data, result
        )
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )

    def test_lesson_retrieve(self):
        url = reverse('materials:lesson-retrieve', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), self.lesson.name
        )

    def test_lesson_create(self):
        url = reverse('materials:lesson-create')
        data = {
            'name': 'scheduler'
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse('materials:lesson-update', args=(self.lesson.pk,))
        data = {
            'name': 'Go'
        }
        response = self.client.patch(url, data)
        data = response.json()

        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('name'), 'Go'
        )

    def test_lesson_delete(self):
        url = reverse('materials:lesson-destroy', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )


class SubscribeTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='admin@admin.com')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(name='Go')

    def test_subscribe_create(self):
        url = reverse('materials:subscribe-create')
        data = {
            'user': self.user.id,
            'course': self.course.id
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(), {'Message': 'Subscription added'}
        )

    def test_subscribe_delete(self):
        url = reverse('materials:subscribe-create')
        data = {
            'user': self.user.id,
            'course': self.course.id
        }
        Subscribe.objects.create(course=self.course, user=self.user)
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(), {'Message': 'Subscription deleted'}
        )
