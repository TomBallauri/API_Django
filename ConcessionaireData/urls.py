from django.urls import path

from ConcessionaireData.views import (
    ProductListView,
    ProductDetailView,
    CommentListCreateView,
    CommentDetailView,
)

#ConcessionaireData/urls.py

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('products/<int:product_pk>/comments/', CommentListCreateView.as_view(), name='Comment-list-create'),
    path('products/<int:product_pk>/comments/<int:pk>', CommentDetailView.as_view(), name='Comment-detail'),

]