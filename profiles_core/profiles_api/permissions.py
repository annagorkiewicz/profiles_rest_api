from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit thier own profile"""

    def has_object_permission(self, request, view, obj):
         """Check user is trying to edit their own profile
         users are able to see other users profile,
         users can edit only their own profile"""
         if request.method in permissions.SAFE_METHODS:
             return True

         return obj.id == request.user.id
