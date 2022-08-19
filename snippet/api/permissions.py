
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from userapp.permissions import Iscustomer, Ismanager
from rest_framework.views import APIView
class PermissionViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [IsAuthenticated],
                                    'update': [IsAuthenticated],
                                    'destroy':[IsAuthenticated],
                                    }
    def get_permissions(self):
        try:
            if self.request.user.is_superuser:

                raise KeyError
            # return permission_classes depending on action 
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError: 
            # when exception occure jump to default permission_classes
            return [permission() for permission in self.permission_classes]

class PermissionViewSetManager(PermissionViewSet):
    permission_classes_by_action = {
                                    'create': [IsAuthenticated,Ismanager],
                                    'update': [IsAuthenticated,Ismanager],
                                    'destroy':[IsAuthenticated,Ismanager],
                                    }

class PermissionViewSetCustomer(PermissionViewSet):
    permission_classes_by_action = {'create': [IsAuthenticated,Iscustomer],
                                    'update': [IsAuthenticated,Iscustomer],
                                    'destroy':[IsAuthenticated,Iscustomer],
                                    }







class PermissionViewApi(APIView):
    permission_classes_by_action = {
                                    'post': [IsAuthenticated],
                                    'put': [IsAuthenticated],
                                    'delete':[IsAuthenticated],
                                    }
    def get_permissions(self):
        
        try:
            if self.request.user.is_superuser:

                raise KeyError
            # return permission_classes depending on action 
            return [permission() for permission in self.permission_classes_by_action[self.request.method.lower()]]
        except KeyError: 
            # when exception occure jump to default permission_classes
            return [permission() for permission in self.permission_classes]

class PermissionViewApiManager(PermissionViewApi):
    permission_classes_by_action = {
                                    'post': [IsAuthenticated,Ismanager],
                                    'put': [IsAuthenticated,Ismanager],
                                    'delete':[IsAuthenticated,Ismanager],
                                    }

class PermissionViewApiCustomer(PermissionViewApi):
    permission_classes_by_action = {
    
                                    'get': [IsAuthenticated,Iscustomer],
                                    'post': [IsAuthenticated,Iscustomer],
                                    'put': [IsAuthenticated,Iscustomer],
                                    'delete':[IsAuthenticated,Iscustomer],
                                    }