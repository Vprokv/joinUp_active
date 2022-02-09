from django.urls import path, include

from .api_views import (
    AdaptationProgramAPIView,
    AdaptationProgramDetailAPIView,

    EmployeeAPIView,
    EmployeeDetailAPIView,

    AdaptationStageAPIView,
    AdaptationStageDetailAPIView,

    BlockPIView,
    BlockDetailAPIView,

    LevelAPIView,
    LevelDetailAPIView,

    GoalAPIView,
    GoalDetailAPIView,

    DocumentAPIView,
    DocumentDetailAPIView,

    ContactAPIView,
    ContactDetailAPIView,

    CustomerAPIView,
    CustomerDetailAPIView,
    LicensePackAPIView,
    LicensePackDetailAPIView,
    LicenseAPIView,
    LicenseDetailAPIView,
    UserCandidateAPIView,
    UserCandidateDetailAPIView,
    CandidateAPIView,
    CandidateDetailAPIView,
    AdaptationStatusAPIView,
    AwardAPIView,
    AwardCandidateAPIView,
    MessageAPIView,
    CandidateAPIViewFilter,
    JobDirectoryAPIView,
    JobDirectoryDetailAPIView,
    CommentToStageAPIView,
    FileView
    # upload
)

urlpatterns = [
    # path('user/candidate/', UserCandidateAPIView.as_view(), name='user candidate'),
    # path('user/candidate/<str:id>/', UserCandidateDetailAPIView.as_view(), name='user candidate detail'),
    #
    # path('user/employee/', UserEmployeeAPIView.as_view(), name='user employee'),
    # path('user/employee/<str:id>/', UserEmployeeDetailAPIView.as_view(), name='user employee detail'),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('upload/', FileView.as_view(), name='file-upload'),

    path('candidate/', CandidateAPIView.as_view(), name='candidate employee'),  # any search!
    path('candidate/filter/', CandidateAPIViewFilter.as_view(), name='employee filter for date and any params'),
    # search and filter
    # /api-active/candidate/filter/?post=разработчик&first_name=vv&status=1
    # /api-active/candidate/filter/?search=разработчик&first_name=vv&status=1
    path('candidate/<str:id>/', CandidateDetailAPIView.as_view(), name='candidate employee detail'),

    path('employee/', EmployeeAPIView.as_view(), name='employee'),
    path('employee/<str:id>/', EmployeeDetailAPIView.as_view(), name='employee detail'),

    path('adaptationprogram/', AdaptationProgramAPIView.as_view(), name='adaptation program'),
    path('adaptationprogram/<str:id>/', AdaptationProgramDetailAPIView.as_view(), name='adaptation program detail'),

    path('adaptationlevel/', LevelAPIView.as_view(), name='level'),
    path('adaptationlevel/<str:id>/', LevelDetailAPIView.as_view(), name='level detail'),

    path('adaptationstage/', AdaptationStageAPIView.as_view(), name='adaptation stage'),
    path('adaptationstage/<str:id>/', AdaptationStageDetailAPIView.as_view(), name='adaptation stage detail'),

    path('adaptationblock/', BlockPIView.as_view(), name='block'),
    path('adaptationblock/<str:id>/', BlockDetailAPIView.as_view(), name='block detail'),

    path('adaptationbgoal/', GoalAPIView.as_view(), name='goal'),
    path('adaptationbgoal/<str:id>/', GoalDetailAPIView.as_view(), name='goal detail'),

    path('adaptationdocument/', DocumentAPIView.as_view(), name='document'),
    path('adaptationdocument/<str:id>/', DocumentDetailAPIView.as_view(), name='document detail'),

    path('adaptationcontact/', ContactAPIView.as_view(), name='contact'),
    path('adaptationcontact/<str:id>/', ContactDetailAPIView.as_view(), name='contact detail'),

    path('customer/', CustomerAPIView.as_view(), name='customer'),
    path('customer/<str:id>/', CustomerDetailAPIView.as_view(), name='customer detail'),

    path('directory/', JobDirectoryAPIView.as_view(), name='job directory catalog'),
    path('directory/<str:id>/', JobDirectoryDetailAPIView.as_view(), name='job directory catalog'),

    path('adaptationstatus/', AdaptationStatusAPIView.as_view(), name='adaptation status'),
    path('adaptationstatus/<str:id>/', AdaptationStatusAPIView.as_view(), name='adaptation status detail'),

    path('comment/', CommentToStageAPIView.as_view(), name='adaptation stage comment'),
    path('comment/<str:id>/', CommentToStageAPIView.as_view(), name='adaptation stage comment'),

    # path('licensepack/', LicensePackAPIView.as_view(), name='license pack'),
    # path('licensepack/<str:id>/', LicensePackDetailAPIView.as_view(), name='license pack detail'),
    #
    # path('license/', LicenseAPIView.as_view(), name='license pack'),
    # path('licensepaclicensek/<str:id>/', LicenseDetailAPIView.as_view(), name='license pack detail'),

    path('award/', AwardAPIView.as_view(), name='award '),
    path('award/<str:id>/', AwardAPIView.as_view(), name='award detail'),
    #
    # path('awardcandidate/', AwardCandidateAPIView.as_view(), name='award candidate '),
    # path('awardcandidate/<str:id>/', AwardCandidateAPIView.as_view(), name='award candidate detail'),
    #
    # path('message/', MessageAPIView.as_view(), name='message'),
    # path('message/<str:id>/', MessageAPIView.as_view(), name='message detail')
]
