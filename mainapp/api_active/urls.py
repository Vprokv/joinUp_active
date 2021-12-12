from django.urls import path

from .api_views import AdaptationProgramAPIView, AdaptationProgramDetailAPIView

urlpatterns = [
    path('adaptationprogram/', AdaptationProgramAPIView.as_view(), name='adaptation program'),
    path('adaptationprogram/<str:id>/', AdaptationProgramDetailAPIView.as_view(), name='adaptation program detail'),
]
