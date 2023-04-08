from rest_framework import routers
from .viewsets import RegisterViewSet


router = routers.DefaultRouter()
router.register(r'auth/register', RegisterViewSet, basename='auth-register')

urlpatterns = [
    *router.urls,
]
