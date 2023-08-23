from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission class for admin access or read-only access.

    Allows full access to superusers and read-only access to authenticated users for non-safe methods.

    Attributes:
        None

    Methods:
        has_permission: Determine if the user has the required permission.
    """

    def has_permission(self, request, view):
        """
        Check if the user has permission to perform the action.

        Args:
            request (HttpRequest): The request object.
            view (APIView): The view associated with the action.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
            return True
        return request.user and request.user.is_superuser
