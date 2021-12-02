from django.urls import path

from .views import (
    ProgramTestAPIView,
    AdaptationProgramTestAPIView,
    AdaptationLevelTestAPIView,
    AdaptationStageTestAPIView,
    AdaptationBlockTestAPIView,
    AdaptationGoalTestAPIView,
    AdaptationDocumentTestAPIView,
    AdaptationContactTestAPIView,
    LnkLevelProgramTestAPIView,
    LnkStageLevelTestAPIView,
    LnkGoalProgramTestAPIView,
    LnkDocumentProgramTestAPIView,
    LnkContactProgramTestAPIView,
    # CustomerTestAPIView,
    # LicensePackTestAPIView,
    # UserServiceUserTestAPIView,
    UserServiceSMSTestAPIView,
    UserServiceTokenTestAPIView,
    # UserServiceCandidateTestAPIView,
    # EmployeeTestAPIView,
    IEmployeeServiceAuthenticationTestAPIView,
    RequestUserToken,
    IAdaptationProgramTestAPIView,
    ILevelStagesTestAPIView,
    IGoalsTestAPIView,
    IDocumentsTestAPIView,
    IContactsTestAPIView,
    IBlocksTestAPIView
)

# http://127.0.0.1:8000/api/
urlpatterns = [
    path('program/', ProgramTestAPIView.as_view(), name='program'),
    # Сервис old
    # IAdaptationProgramService
    path('adaptationprogram/', AdaptationProgramTestAPIView.as_view(), name='adaptation program'),
    path('adaptationlevel/', AdaptationLevelTestAPIView.as_view(), name='adaptation level'),
    path('adaptationstage/', AdaptationStageTestAPIView.as_view(), name='adaptation stage'),
    path('adaptationblock/', AdaptationBlockTestAPIView.as_view(), name='adaptation block'),
    path('adaptationbgoal/', AdaptationGoalTestAPIView.as_view(), name='adaptation goal'),
    path('adaptationdocument/', AdaptationDocumentTestAPIView.as_view(), name='adaptation document'),
    path('adaptationcontact/', AdaptationContactTestAPIView.as_view(), name='adaptation contact'),
    path('lnklevelprogram/', LnkLevelProgramTestAPIView.as_view(), name='lnk level program'),
    path('lnkstagelevel/', LnkStageLevelTestAPIView.as_view(), name='lnk stage level'),
    path('lnkgoalprogram/', LnkGoalProgramTestAPIView.as_view(), name='lnk goal program'),
    path('lnkdocumentprogram/', LnkDocumentProgramTestAPIView.as_view(), name='lnk document program'),
    path('lnkpcontactrogram/', LnkContactProgramTestAPIView.as_view(), name='lnk contact program'),
    # IСustomerService
    # path('customer/', CustomerTestAPIView.as_view(), name='customer'),
    # path('licensepack/', LicensePackTestAPIView.as_view(), name='license Pack'),
    # IUserService
    # path('userservice/user/', UserServiceUserTestAPIView.as_view(), name='user service(user)'),
    path('userservice/sms/', UserServiceSMSTestAPIView.as_view(), name='user service(sms)'),
    path('userservice/token/', UserServiceTokenTestAPIView.as_view(), name='user service(token)'),
    # path('userservice/candidate/', UserServiceCandidateTestAPIView.as_view(), name='candidate'),
    # IEmployeeService
    # path('employee/', EmployeeTestAPIView.as_view(), name='candidate'),

    #     Сервисы для мобильного
    path('iemployeeserviceauthentification/', IEmployeeServiceAuthenticationTestAPIView.as_view(),
         name='service authentication'),
    path('requestusercandidatetoken/', RequestUserToken.as_view(), name='request user candidate token'),
    path('iadaptationprogram/', IAdaptationProgramTestAPIView.as_view(), name='i adaptation program'),
    path('ilevelstages/', ILevelStagesTestAPIView.as_view(), name='i level stages'),
    path('igoals/', IGoalsTestAPIView.as_view(), name='i goals'),
    path('idocuments/', IDocumentsTestAPIView.as_view(), name='i documents'),
    path('icontacts/', IContactsTestAPIView.as_view(), name='i contacts'),
    path('iblocks/', IBlocksTestAPIView.as_view(), name='i blocks')
]
