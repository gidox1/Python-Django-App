from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users edit just their own profile"""

    def has_object_permission(selff, request, view, obj):
        """check if user is trying to edit their ow profile"""

        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.id == request.user.id 


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user istrying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id