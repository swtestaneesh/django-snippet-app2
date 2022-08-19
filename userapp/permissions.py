#https://stackoverflow.com/questions/19773869/django-rest-framework-separate-permissions-per-methods
#https://stackoverflow.com/questions/66756584/add-the-permissions-to-the-group-django-rest-framework
#https://stackoverflow.com/questions/45280248/django-rest-framework-group-based-permissions-for-individual-views
#https://www.django-rest-framework.org/api-guide/permissions/
from rest_framework import permissions

class Iscustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='customer'):
            return True
        return False


class Ismanager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='manager'):
            return True
        return False