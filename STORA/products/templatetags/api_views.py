from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from STORA.products.models import Product
from STORA.products.serializers import ProductSerializer


class ProductListAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Product.objects.prefetch_related('barcode').all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)