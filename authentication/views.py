from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from authentication.models import AuthorUser
from authentication.serializers import AuthorUserSerializer


# Create your views here.
# authentication app

class AuthorUserView(APIView):
    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        users = AuthorUser.objects.all()
        serializer = AuthorUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = AuthorUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

