from django.urls import path
from .api_views import (
    EmployeeAuth,
    CandidateAuth,
    CandidateMe
)

urlpatterns = [
    path('employee/', EmployeeAuth.as_view(), name='EmployeeAuth'),
    path('candidate/', CandidateAuth.as_view(), name='TwoFactorAuth'),
    path('me/', CandidateMe.as_view(), name='getMe'),
]
