from django.urls import path

from .api_views import (
    AdaptationProgramAPIView,
    AdaptationProgramDetailAPIView,

    EmployeeAPIView,
    EmployeeDetailAPIView,

    AdaptationStageAPIView,
    AdaptationStageDetailAPIView,

    LevelAPIView,
    LevelDetailAPIView,

    GoalAPIView,
    GoalDetailAPIView,

    DocumentAPIView,
    DocumentDetailAPIView,

    ContactAPIView,
    ContactDetailAPIView,

)

urlpatterns = [
    path('adaptationprogram/', AdaptationProgramAPIView.as_view(), name='adaptation program'),
    path('adaptationprogram/<str:id>/', AdaptationProgramDetailAPIView.as_view(), name='adaptation program detail'),

    path('employee/', EmployeeAPIView.as_view(), name='employee'),
    path('employee/<str:id>/', EmployeeDetailAPIView.as_view(), name='employee detail'),

    path('level/', LevelAPIView.as_view(), name='level'),
    path('level/<str:id>/', LevelDetailAPIView.as_view(), name='level detail'),

    path('adaptationstage/', AdaptationStageAPIView.as_view(), name='adaptation stage'),
    path('adaptationstage/<str:id>/', AdaptationStageDetailAPIView.as_view(), name='adaptation stage detail'),

    path('block/', LevelAPIView.as_view(), name='block'),
    path('block/<str:id>/', LevelDetailAPIView.as_view(), name='block detail'),

    path('goal/', GoalAPIView.as_view(), name='goal'),
    path('goal/<str:id>/', GoalDetailAPIView.as_view(), name='goal detail'),

    path('document/', DocumentAPIView.as_view(), name='document'),
    path('document/<str:id>/', DocumentDetailAPIView.as_view(), name='document detail'),

    path('contact/', ContactAPIView.as_view(), name='contact'),
    path('contact/<str:id>/', ContactDetailAPIView.as_view(), name='contact detail'),

]
