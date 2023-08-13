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
    

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.is_deleted:
            return Response({"detail": "This workplace is already deleted."}, status=status.HTTP_400_BAD_REQUEST)
        
        instance.is_deleted = True
        instance.save()
        
        return Response(status=status.HTTP_204_NO_CONTENT)