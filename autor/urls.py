from .views import AutorView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', AutorView, basename='autor')

urlpatterns = router.urls