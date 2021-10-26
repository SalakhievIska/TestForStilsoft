from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('sections', views.SectionViewSet)
router.register('students-in-sections', views.StudentInSectionViewSet)

urlpatterns = router.urls
