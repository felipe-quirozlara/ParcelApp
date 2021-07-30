from rest_framework import generics
from parcel.models import Envio
from .serializers import EnvioSerializer
from rest_framework.permissions import BasePermission, DjangoModelPermissions, SAFE_METHODS
# Create your views here.
class PostUserWritePermission(BasePermission):
    message = 'Editing post is restricted to the author only'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.cliente == request.user 
    
            
class EnvioList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer
    

class EnvioDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer

