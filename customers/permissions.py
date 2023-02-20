from rest_framework.permissions import BasePermission


class CustomerOnly(BasePermission):
    """
    Base Permission Class For Customer
    """

    def has_object_permission(self, request, view, obj):
        return request.user == obj
