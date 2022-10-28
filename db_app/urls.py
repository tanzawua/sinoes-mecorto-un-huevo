from rest_framework import routers
from .api import ServicioviewSet


router = routers.DefaultRouter()
router.register('api/db_app',ServicioviewSet, 'db_app')

urlpatterns = router.urls