from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from menu.serializers import MenuSerializer
from menu.models import Menu




class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer




# Create your views here.
