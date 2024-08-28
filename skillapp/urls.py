from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SkillClassViewSet, ReviewViewSet, EnrollmentViewSet, UserViewSet


router = DefaultRouter()
router.register(r'skillclasses', SkillClassViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]