from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if request.user.student:
            return True
        else:
            return False

class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if request.user.profile.role == 'teacher':
            return True
        else:
            return False