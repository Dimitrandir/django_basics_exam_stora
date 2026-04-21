from rest_framework import serializers

from STORA.deliveries.models import DeliveryAttributes, DeliveryItems


class DeliveryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryItems
        fields = [
            'id',
            'delivery_item',
            'delivery_quantity',
            'price_at_delivery',
            'total_price_row',
        ]


class DeliveryAttributesSerializer(serializers.ModelSerializer):
    items = DeliveryItemSerializer(many=True, read_only=True)

    class Meta:
        model = DeliveryAttributes
        fields = [
            'id',
            'receiver',
            'time_of_delivery',
            'supplier',
            'document_type',
            'document_number',
            'document_date',
            'items',
        ]