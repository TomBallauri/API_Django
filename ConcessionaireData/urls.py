from django.urls import path

from ConcessionaireData.views import (
    ConcessionnaireListView,
    ConcessionnaireDetailView,
    ConcessionnaireVehiculesListView,
    ConcessionnaireVehiculeDetailView,
)

# ConcessionaireData/urls.py

urlpatterns = [
    # Concessionnaire / Vehicule endpoints
    path('concessionnaires/', ConcessionnaireListView.as_view(), name='concessionnaire-list'),
    path('concessionnaires/<int:pk>/', ConcessionnaireDetailView.as_view(), name='concessionnaire-detail'),
    path('concessionnaires/<int:concessionnaire_pk>/vehicules/', ConcessionnaireVehiculesListView.as_view(), name='concessionnaire-vehicules-list'),
    path('concessionnaires/<int:concessionnaire_pk>/vehicules/<int:pk>/', ConcessionnaireVehiculeDetailView.as_view(), name='concessionnaire-vehicule-detail'),
]