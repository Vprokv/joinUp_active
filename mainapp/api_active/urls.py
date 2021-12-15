from django.urls import path

from .api_views import (
    AdaptationProgramAPIView,
    AdaptationProgramDetailAPIView,

    EmployeeAPIView,
    EmployeeDetailAPIView,

    LevelAPIView,
    LevelDetailAPIView
)

urlpatterns = [
    path('adaptationprogram/', AdaptationProgramAPIView.as_view(), name='adaptation program'),
    path('adaptationprogram/<str:id>/', AdaptationProgramDetailAPIView.as_view(), name='adaptation program detail'),

    path('employee/', EmployeeAPIView.as_view(), name='employee'),
    path('employee/<str:id>/', EmployeeDetailAPIView.as_view(), name='employee detail'),

    path('level/', LevelAPIView.as_view(), name='level'),
    path('level/<str:id>/', LevelDetailAPIView.as_view(), name='level detail'),

    path('adaptationstage/', LevelAPIView.as_view(), name='level'),
    path('adaptationstage/<str:id>/', LevelDetailAPIView.as_view(), name='level detail'),
]
