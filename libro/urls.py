from .views import LibroView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', LibroView, basename='libro')

urlpatterns = router.urls