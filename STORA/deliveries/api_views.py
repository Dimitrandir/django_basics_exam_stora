from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from STORA.deliveries.models import DeliveryAttributes
from STORA.deliveries.serializers import DeliveryAttributesSerializer


class DeliveryListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        deliveries = DeliveryAttributes.objects.prefetch_related('items').all()
        serializer = DeliveryAttributesSerializer(deliveries, many=True)
        return Response(serializer.data)