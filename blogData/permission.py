from rest_framework.permissions import BasePermission
from django.utils import timezone
from datetime import timedelta

class IsAuthorOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.author or request.user.is_staff

class IsAdminForProduct(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff

class IsCommentAuthorOrAdminWithin24h(BasePermission):
    message = "Vous ne pouvez éditer ce commentaire que dans les 24h suivant sa création."

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            if timezone.now() - obj.date_creation > timedelta(minutes=5):
                self.message = "Le délai de modification (24h) est dépassé."
                return False
            return True
        return request.user.is_staff