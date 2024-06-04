from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Course
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='admin@admin.com')
        self.client.force_authenticate(user=self.user)
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
