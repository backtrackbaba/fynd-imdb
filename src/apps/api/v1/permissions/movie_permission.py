from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomIsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a an admin, or is a read-only request.

    This is used to ensure that any user, even anonymous users can read but only the admin/staff can modify it.
    Even authenticated, non-staff user cannot edit the data.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )
