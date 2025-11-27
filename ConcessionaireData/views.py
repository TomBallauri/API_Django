from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.permissions import AllowAny, IsAdminUser

from .models import Concessionnaire, Vehicule
from .serializers import (
    ConcessionnaireSerializer,
    VehiculeSerializer,
    ConcessionnaireCreateSerializer,
)
#/Concessionnaire
class ConcessionnaireListView(APIView):

    # Laisse tout le monde lire, mais restreint les modifs aux admin
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get(self, request):
        qs = Concessionnaire.objects.all()
        serializer = ConcessionnaireSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ConcessionnaireCreateSerializer(data=request.data)
        if serializer.is_valid():
            inst = serializer.save()
            out = ConcessionnaireSerializer(inst)
            return Response(out.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

#/Concessionnaire/<int:id>
class ConcessionnaireDetailView(APIView):

    # Laisse tout le monde lire, mais restreint les modifs aux admin
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get(self, request, pk):
        concessionnaire = get_object_or_404(Concessionnaire, pk=pk)
        serializer = ConcessionnaireSerializer(concessionnaire)
        return Response(serializer.data)

    def put(self, request, pk):
        concessionnaire = get_object_or_404(Concessionnaire, pk=pk)
        serializer = ConcessionnaireCreateSerializer(concessionnaire, data=request.data)
        if serializer.is_valid():
            inst = serializer.save()
            out = ConcessionnaireSerializer(inst)
            return Response(out.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        concessionnaire = get_object_or_404(Concessionnaire, pk=pk)
        concessionnaire.delete()
        return Response(status=HTTP_204_NO_CONTENT)


#/Concessionnaire/<int:id>/vehicules
class ConcessionnaireVehiculesListView(APIView):

    # Laisse tout le monde lire, mais restreint les modifs aux admin
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get(self, request, concessionnaire_pk):
        concessionnaire = get_object_or_404(Concessionnaire, pk=concessionnaire_pk)
        vehicules = concessionnaire.vehicules.all()
        serializer = VehiculeSerializer(vehicules, many=True)
        return Response(serializer.data)

    def post(self, request, concessionnaire_pk):
        concessionnaire = get_object_or_404(Concessionnaire, pk=concessionnaire_pk)
        serializer = VehiculeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(concessionnaire=concessionnaire)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

#/Concessionnaire/<int:id>/vehicules/<int:pk>
class ConcessionnaireVehiculeDetailView(APIView):

    # Laisse tout le monde lire, mais restreint les modifs aux admin
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

    def get(self, request, concessionnaire_pk, pk):
        concessionnaire = get_object_or_404(Concessionnaire, pk=concessionnaire_pk)
        vehicule = get_object_or_404(Vehicule, pk=pk, concessionnaire=concessionnaire)
        serializer = VehiculeSerializer(vehicule)
        return Response(serializer.data)

    def put(self, request, concessionnaire_pk, pk):
        concessionnaire = get_object_or_404(Concessionnaire, pk=concessionnaire_pk)
        vehicule = get_object_or_404(Vehicule, pk=pk, concessionnaire=concessionnaire)
        serializer = VehiculeSerializer(vehicule, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, concessionnaire_pk, pk):
        concessionnaire = get_object_or_404(Concessionnaire, pk=concessionnaire_pk)
        vehicule = get_object_or_404(Vehicule, pk=pk, concessionnaire=concessionnaire)
        vehicule.delete()
        return Response(status=HTTP_204_NO_CONTENT)
