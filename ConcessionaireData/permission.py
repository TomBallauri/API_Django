from rest_framework.permissions import BasePermission
from django.utils import timezone
from datetime import timedelta

class IsAdminForConcessionnaire(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff

class IsAdminForVehicule(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff