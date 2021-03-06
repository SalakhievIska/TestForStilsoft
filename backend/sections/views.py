from rest_framework.viewsets import ModelViewSet
from .serializers import SectionSerializer, StudentInSectionSerializer
from .models import Section, StudentInSection
from .filters import SectionFilter


class SectionViewSet(ModelViewSet):
    """
    ViewSet для работы с секциями
    """

    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    filterset_class = SectionFilter


class StudentInSectionViewSet(ModelViewSet):
    """
    ViewSet для зачисления в секции и отчисления из секций студентов
    """

    queryset = StudentInSection.objects.all()
    serializer_class = StudentInSectionSerializer
