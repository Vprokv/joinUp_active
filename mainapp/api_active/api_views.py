from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from .serializers import (
    ProgramSerializer,
    EmployeeSerializer,
    LevelSerializer,
    AdaptationStageSerializer,
)
from ..models import (
    Program,
    Employee,
    Level,
    AdaptationStage
)


class PaginationBaseClass(PageNumberPagination):
    page_size = 11
    page_query_param = 'page_size'
    max_page_size = 20


class AdaptationProgramAPIView(ListCreateAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()


class AdaptationProgramDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    lookup_field = 'id'


class EmployeeAPIView(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    filter_backends = [SearchFilter]
    search_fields = [
        'last_name',
        'first_name',
        'middle_name',
        'post',
        'status',
        'create_date'
    ]


class EmployeeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    lookup_field = 'id'


class LevelAPIView(ListCreateAPIView):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()
    filter_backends = [SearchFilter]
    search_fields = [
        'id_program',
        'status',
        'create_date'
    ]
    # TODO search id_level


class LevelDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()
    lookup_field = 'id'


class AdaptationStageAPIView(ListCreateAPIView):
    serializer_class = AdaptationStageSerializer
    queryset = AdaptationStage.objects.all()
    filter_backends = [SearchFilter]
    search_fields = [
        'status',
        'create_date'
    ] # TODO search id_level


class AdaptationStageDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdaptationStageSerializer
    queryset = Level.objects.all()
    lookup_field = 'id'
