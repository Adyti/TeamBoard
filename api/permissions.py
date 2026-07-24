from rest_framework.permissions import BasePermission


class IsCompanyAdmin(BasePermission):
    """
    Allows access only to companies with the 'admin' role.
    """

    def has_permission(self, request, view):

        if not request.user.is_authenticated:
            return False

        return request.user.company.role == "admin"