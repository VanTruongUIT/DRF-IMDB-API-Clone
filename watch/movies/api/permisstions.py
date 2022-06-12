from email import message
from rest_framework import permissions

# https://testdriven.io/blog/drf-permissions/
class AdminOrReadOnly(permissions.IsAdminUser):
    message = "Only admin can perform the post request!!!"
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True 
        else:
            return bool(request.user and request.user.is_staff)
    
    

class AuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True 
        else:
            return obj.author == request.user