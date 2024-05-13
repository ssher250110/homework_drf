from django.urls import path
from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView

router = SimpleRouter()
router.register('', CourseViewSet)

app_name = MaterialsConfig.name

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
] + router.urls
