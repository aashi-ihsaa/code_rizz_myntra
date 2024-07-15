from rest_framework import permissions

class IsGenZUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the Gen-Z profile
        return obj.user == request.user
