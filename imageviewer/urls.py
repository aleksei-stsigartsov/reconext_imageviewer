from rest_framework import routers
from .api import ImageViewSet

router = routers.DefaultRouter()
router.register('api/image', ImageViewSet, 'image')


urlpatterns = router.urls