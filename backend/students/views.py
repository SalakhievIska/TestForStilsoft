from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer
from .models import Student
from .filters import StudentFilter


class StudentViewSet(ModelViewSet):
    """
    ViewSet для работы со студентами
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filterset_class = StudentFilter
