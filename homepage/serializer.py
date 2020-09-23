from rest_framework import serializers
from homepage.models import Shoe


class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = [
            'id',
            'size',
            'brand_name',
            'material',
            'fasten_type',
            'manufacturer',
            'color',
            'shoe_type',
        ]