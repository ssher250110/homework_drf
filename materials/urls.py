from rest_framework.routers import SimpleRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet

router = SimpleRouter()
router.register('', CourseViewSet)

app_name = MaterialsConfig.name

urlpatterns = [

] + router.urls
