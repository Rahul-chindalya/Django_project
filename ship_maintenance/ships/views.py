from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

from .serializer import ShipSerializer
from .models import Ship
from .permission import ISAdminOrEngineer

# Create your views here.

