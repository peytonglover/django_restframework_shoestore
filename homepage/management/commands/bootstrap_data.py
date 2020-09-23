from django.core.management.base import BaseCommand
from homepage.models import ShoeType, ShoeColor

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        types = [
            'sneaker',
            'boot',
            'sandal',
            'dress',
            'other',
        ]

        color = [
            'Red',
            'Orange',
            'Yellow',
            'Green',
            'Blue',
            'Indigo',
            'Violet',
            'White',
            'Black'
        ]

        for item in types:
            ShoeType.objects.create(style=item)

        for color in color:
            ShoeColor.objects.create(color_name=color)