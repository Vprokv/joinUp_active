from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from .serializers import ProgramSerializer
from ..models import Program


class ProgramPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 10


class AdaptationProgramAPIView(ListCreateAPIView):
    serializer_class = ProgramSerializer
    pagination_class = ProgramPagination
    queryset = Program.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['id_customer', 'id', 'status', 'create_date']


class AdaptationProgramDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
    lookup_field = 'id'
