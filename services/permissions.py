from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsVendorOrAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if not request.user.is_authenticated:
            return False

        if request.user.role == "admin":
            return True

        if request.user.role == "vendor":
            return True

        return False
