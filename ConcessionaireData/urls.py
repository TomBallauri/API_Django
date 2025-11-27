from django.urls import path

from ConcessionaireData.views import (
    ConcessionnaireListView,
    ConcessionnaireDetailView,
    ConcessionnaireVehiculesListView,
    ConcessionnaireVehiculeDetailView,
)
from ConcessionaireData.views import AuthorUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# ConcessionaireData/urls.py

urlpatterns = [
    # Concessionnaire / Vehicule endpoints
    path('concessionnaires/', ConcessionnaireListView.as_view(), name='concessionnaire-list'),
    path('concessionnaires/<int:pk>/', ConcessionnaireDetailView.as_view(), name='concessionnaire-detail'),
    path('concessionnaires/<int:concessionnaire_pk>/vehicules/', ConcessionnaireVehiculesListView.as_view(), name='concessionnaire-vehicules-list'),
    path('concessionnaires/<int:concessionnaire_pk>/vehicules/<int:pk>/', ConcessionnaireVehiculeDetailView.as_view(), name='concessionnaire-vehicule-detail'),
    # Authentication / bonus endpoints
    path('users/', AuthorUserView.as_view(), name='user-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
]