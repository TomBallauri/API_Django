from django.urls import path

from ConcessionaireData.views import (
    ProductListView,
    ProductDetailView,
    CommentListCreateView,
    CommentDetailView,
    ConcessionnaireListView,
    ConcessionnaireDetailView,
    ConcessionnaireVehiculesListView,
    ConcessionnaireVehiculeDetailView,
)

#ConcessionaireData/urls.py

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:product_pk>/comments/', CommentListCreateView.as_view(), name='Comment-list-create'),
    path('products/<int:product_pk>/comments/<int:pk>', CommentDetailView.as_view(), name='Comment-detail'),
    # Concessionnaire / Vehicule endpoints
    path('concessionnaires/', ConcessionnaireListView.as_view(), name='concessionnaire-list'),
    path('concessionnaires/<int:pk>/', ConcessionnaireDetailView.as_view(), name='concessionnaire-detail'),
    path('concessionnaires/<int:concessionnaire_pk>/vehicules/', ConcessionnaireVehiculesListView.as_view(), name='concessionnaire-vehicules-list'),
    path('concessionnaires/<int:concessionnaire_pk>/vehicules/<int:pk>/', ConcessionnaireVehiculeDetailView.as_view(), name='concessionnaire-vehicule-detail'),
]