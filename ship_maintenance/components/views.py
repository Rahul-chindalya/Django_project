from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from .serializer import ComponentSerializer
from .models import Component
from .models import 


# Create your views here.
