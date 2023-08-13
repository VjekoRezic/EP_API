from rest_framework import viewsets
from .models import Workplace
from .serializers import WorkplaceSerializer
from user.permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from user.authentication import CustomUserAuth

class WorkplaceViewSet(viewsets.ModelViewSet):
    authentication_classes = (CustomUserAuth,)
    permission_classes = [IsAdminOrReadOnly]
    queryset = Workplace.objects.filter( is_deleted = False)
    serializer_class = WorkplaceSerializer
    
    def get_queryset(self):
        # Only include objects where is_deleted is False
        return Workplace.objects.filter(is_deleted=False)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        
        return Response(status=status.HTTP_204_NO_CONTENT)