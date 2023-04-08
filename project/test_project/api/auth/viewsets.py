from .serializers import RegisterSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response


class RegisterViewSet(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            "user": serializer.data, 
        }, status=status.HTTP_201_CREATED)
