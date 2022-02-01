import django_filters
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, APi
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from django.views.generic import TemplateView
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from rest_framework.permissions import IsAuthenticated

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
    ContactSerializer,
    CustomerSerializer,
    LicensePackSerializer,
    LicenseSerializer,
    UserCandidateSerializer,
    CandidateSerializer,
    AdaptationStatusSerializer,
    AwardSerializer,
    AwardCandidateSerializer,
    MessageSerializer,
    EmployeeSerializerDetail,
    ICandidateSerializer,
    CandidateSerializerDetail,
    UserCandidateDetailSerializer,
    JobDirectorySerializer, CommentToStageSerializer
)
from ..models import (
    Program,
    Employee,
    Level,
    AdaptationStage,
    Block,
    Goal,
    Document,
    Contact,
    LicensePack,
    Customer,
    License,
    UserCandidate,
    Candidate,
    AdaptationStatus,
    Award,
    AwardCandidate,
    Message,
    JobDirectoryCatalogs, CommentToStage
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
    filter_fields = [
        'id_customer',
        'status',
        'create_date'
    ]


class AdaptationProgramDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProgramDetailSerializer
    queryset = Program.objects.all()
    lookup_field = 'id'


# search
class EmployeeAPIView(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    filter_backends = [SearchFilter]
    # permission_classes = [IsAuthenticated]
    search_fields = [
        'last_name',
        'first_name',
        'middle_name',
        'post',
        'status',
        'create_date'
    ]


class EmployeeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializerDetail
    queryset = Employee.objects.all()
    lookup_field = 'id'


class LevelAPIView(ListCreateAPIView):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['program', 'status', 'create_date'],

    filter_fields = [
        'program',
        'status',
        'create_date'
    ]


class LevelDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LevelSerializer
    queryset = Level.objects.all()
    lookup_field = 'id'


class AdaptationStageAPIView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = AdaptationStageSerializer
    queryset = AdaptationStage.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = [
        'status',
        'create_date',
        'level'
    ]
    filter_fields = [
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
    filter_backends = [SearchFilter, DjangoFilterBackend]
    # search_fields = [
    #     'status',
    #     'id_stage',
    #     'create_date'
    # ]
    # filter_fields = [
    #     'status',
    #     'create_date'
    # ]


class BlockDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BlockSerializer
    queryset = Block.objects.all()
    lookup_field = 'id'


class GoalAPIView(ListCreateAPIView):
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = [
        'status',
        'program'
        'create_date'
    ]
    filter_fields = [
        'status',
        'create_date'
    ]


class GoalDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = GoalSerializer
    queryset = Goal.objects.all()
    lookup_field = 'id'


class DocumentAPIView(ListCreateAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = [
        'create_date',
        'document_name'
    ]
    filter_fields = [
        'create_date',
        'document_name'
    ]


class DocumentDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    lookup_field = 'id'


class ContactAPIView(ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = [
        'status',
        'create_date'
    ]
    filter_fields = [
        'status',
        'create_date'
    ]


class ContactDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = 'id'


class CustomerAPIView(ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = [
        'customer_name',
        'city',
        'status'
    ]
    filter_fields = [
        'customer_name',
        'city',
        'status'
    ]


class CustomerDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = 'id'


class LicensePackAPIView(ListCreateAPIView):
    serializer_class = LicensePackSerializer
    queryset = LicensePack.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = [
        'users_count',
        'users_spent',
        'status'
    ]
    filter_fields = [
        'users_count',
        'users_spent',
        'status'
    ]


class LicensePackDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LicensePackSerializer
    queryset = LicensePack.objects.all()
    lookup_field = 'id'


class LicenseAPIView(ListCreateAPIView):
    serializer_class = LicenseSerializer
    queryset = License.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = [
        'id_license_pack',
        'id_candidate',
        'start_date',
        'finish_date',
        'status'
    ]
    filter_fields = [
        'id_license_pack',
        'id_candidate',
        'start_date',
        'finish_date',
        'status'
    ]


class LicenseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LicenseSerializer
    queryset = License.objects.all()
    lookup_field = 'id'


class UserCandidateAPIView(ListCreateAPIView):
    serializer_class = UserCandidateSerializer
    queryset = UserCandidate.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]


class UserCandidateDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserCandidateDetailSerializer
    queryset = UserCandidate.objects.all()
    lookup_field = 'id'


class CandidateFilter(django_filters.FilterSet):
    start_before = django_filters.DateTimeFilter(field_name="create_date", lookup_expr="lte")
    start_after = django_filters.DateTimeFilter(field_name="create_date", lookup_expr="gte")

    class Meta:
        model = Candidate
        fields = [
            'last_name',
            'first_name',
            'middle_name',
            'post',
            # 'status',
            'start_before',
            'start_after',
            'create_date',
            'mobile_phone'
        ]


# filter
class CandidateAPIViewFilter(ListCreateAPIView):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()
    filterset_class = CandidateFilter
    filter_backends = [SearchFilter, DjangoFilterBackend]

    search_fields = [
        'last_name',
        'first_name',
        'middle_name',
        'post',
        # 'status',
        'create_date',
        'mobile_phone'
    ]


class CandidateAPIView(ListCreateAPIView):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()
    pagination_class = PaginationBaseClass
    filterset_class = CandidateFilter
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = [
        'last_name',
        'first_name',
        'middle_name',
        'post',
        # 'status',
        'create_date',
        'mobile_phone'
    ]


class CandidateDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CandidateSerializerDetail
    queryset = Candidate.objects.all()
    lookup_field = 'id'


class ICandidateAPIView(ListAPIView):
    serializer_class = ICandidateSerializer
    queryset = Candidate.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    lookup_field = 'id'
    filter_fields = ['candidate']


class AdaptationStatusAPIView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = AdaptationStatusSerializer
    queryset = AdaptationStatus.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    lookup_field = 'id'


class CommentToStageAPIView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = CommentToStageSerializer
    queryset = CommentToStage.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    lookup_field = 'id'


class AwardAPIView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = AwardSerializer
    queryset = Award.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    lookup_field = 'id'


class AwardCandidateAPIView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = AwardCandidateSerializer
    queryset = AwardCandidate.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    lookup_field = 'id'


class MessageAPIView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    lookup_field = 'id'


class JobDirectoryAPIView(ListCreateAPIView):
    serializer_class = JobDirectorySerializer
    queryset = JobDirectoryCatalogs.objects.all()


class JobDirectoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = JobDirectorySerializer
    queryset = JobDirectoryCatalogs.objects.all()
    lookup_field = 'id'


# def upload(request):
#     if request.method == 'POST':
#         uploaded_file = request.FILES['document']
#         fs = FileSystemStorage()
#         fs.save(uploaded_file.name, uploaded_file)
#         return request.name
