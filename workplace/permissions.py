from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET, HEAD, and OPTIONS requests for all users
        print("Provjerava")
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only allow POST requests for administrators
        print (request.user)
        print( request.user.is_staff)
        print( request.user.email )
        return request.user and request.user.is_staff