from rest_framework import permissions


class IsAuthorPermission(permissions.BasePermission):
    """
        Пользовательское разрешение, позволяющее только владельцам поста
        редактировать и удалять его.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
