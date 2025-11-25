from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from ConcessionaireData.models import Product, Comment, Concessionnaire, Vehicule
from ConcessionaireData.permission import IsCommentAuthorOrAdminWithin24h, IsAuthorOrAdmin
from ConcessionaireData.serializers import (
    ProductListSerializer,
    ProductDetailSerializer,
    CommentSerializer,
    ConcessionnaireSerializer,
    VehiculeSerializer,
)


# Create your views here.


# /Products
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        # Serialize and return the Products
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# /Product/<int:id>
class ProductDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        permission = IsAuthorOrAdmin()
        if not permission.has_object_permission(request, self, product):
            raise PermissionDenied()
        serializer = ProductDetailSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        permission = IsAuthorOrAdmin()
        if not permission.has_object_permission(request, self, product):
            raise PermissionDenied()
        product.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class CommentListCreateView(APIView):
    def get(self, request, product_pk):
        product = get_object_or_404(Product, pk=product_pk)
        comments = product.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, product_pk):
        product = get_object_or_404(Product, pk=product_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product, author=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CommentDetailView(APIView):
    def get_object(self, product_pk, pk):
        product = get_object_or_404(Product, pk=product_pk)
        return get_object_or_404(Comment, pk=pk, product=product)

    def get(self, request, product_pk, pk):
        comment = self.get_object(product_pk, pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, product_pk, pk):
        comment = self.get_object(product_pk, pk)
        permission = IsCommentAuthorOrAdminWithin24h()
        if not permission.has_object_permission(request, self, comment):
            raise PermissionDenied(permission.message)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, product_pk, pk):
        comment = self.get_object(product_pk, pk)
        permission = IsCommentAuthorOrAdminWithin24h()
        if not permission.has_object_permission(request, self, comment):
            raise PermissionDenied(permission.message)
        comment.delete()
        return Response(status=HTTP_204_NO_CONTENT)


#/Concessionnaire
class ConcessionnaireListView(APIView):
    def get(self, request):
        qs = Concessionnaire.objects.all()
        serializer = ConcessionnaireSerializer(qs, many=True)
        return Response(serializer.data)

#/Concessionnaire/<int:id>
class ConcessionnaireDetailView(APIView):
    def get(self, request, pk):
        concessionnaire = get_object_or_404(Concessionnaire, pk=pk)
        serializer = ConcessionnaireSerializer(concessionnaire)
        return Response(serializer.data)


class ConcessionnaireVehiculesListView(APIView):
    def get(self, request, concessionnaire_pk):
        concessionnaire = get_object_or_404(Concessionnaire, pk=concessionnaire_pk)
        vehicules = concessionnaire.vehicules.all()
        serializer = VehiculeSerializer(vehicules, many=True)
        return Response(serializer.data)


class ConcessionnaireVehiculeDetailView(APIView):
    def get(self, request, concessionnaire_pk, pk):
        concessionnaire = get_object_or_404(Concessionnaire, pk=concessionnaire_pk)
        vehicule = get_object_or_404(Vehicule, pk=pk, concessionnaire=concessionnaire)
        serializer = VehiculeSerializer(vehicule)
        return Response(serializer.data)
