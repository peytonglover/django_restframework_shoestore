from django.shortcuts import render
from rest_framework import viewsets
from homepage.serializer import ShoeSerializer
from homepage.models import Shoe
# Create your views here.

class ShoeViewSet(viewsets.ModelViewSet):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer