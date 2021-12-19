from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from .serializers import (
    ProgramSerializer,
    ProgramDetailSerializer,
    EmployeeSerializer,
    LevelSerializer,
    AdaptationStageSerializer,
    AdaptationStageDetailSerializer,
    BlockSerializer,
    GoalSerializer,
    DocumentSerializer,
    ContactSerializer
)
from ..models import (
    Program,
    Employee,
    Level,
    AdaptationStage,
    Block,
    Goal,
    Document,
    Contact
)


class PaginationBaseClass(PageNumberPagination):
    page_size = 11
    page_query_param = 'page_size'
    max_page_size = 20


class AdaptationProgramAPIView(ListCreateAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    filter_backends = [SearchFilter]
    search_fields = [
        'id_customer',
        'status',
        'create_date'
    ]


class AdaptationProgramDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProgramDetailSerializer
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
        'program',
        'status',
        'create_date'
    ]


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
        'create_date',
        'level'
    ]


class AdaptationStageDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdaptationStageDetailSerializer
    queryset = AdaptationStage.objects.all()
    lookup_field = 'id'


class BlockPIView(ListCreateAPIView):
    serializer_class = BlockSerializer
    queryset = Block.objects.all()
    filter_backends = [SearchFilter]
    adaptationStage = [
        'status',
        'id_stage',
        'create_date'
    ]


class BlockDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlockSerializer
    queryset = Block.objects.all()
    lookup_field = 'id'


class GoalAPIView(ListCreateAPIView):
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()
    filter_backends = [SearchFilter]
    search_fields = [
        'status',
        'create_date'
    ]  # TODO search id_program


class GoalDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()
    lookup_field = 'id'


class DocumentAPIView(ListCreateAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    filter_backends = [SearchFilter]
    search_fields = [
        'status',
        'create_date'
    ]  # TODO search id_program


class DocumentDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    lookup_field = 'id'


class ContactAPIView(ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = [SearchFilter]
    search_fields = [
        'status',
        'create_date'
    ]  # TODO search id_program


class ContactDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = 'id'
