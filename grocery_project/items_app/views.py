from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Items
from .serializer import ItemSerializer
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
@swagger_auto_schema(method='post',request_body=ItemSerializer)
@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data=request.data)#we are taking the Json data and conveting it in modeldata -deserilizer

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='get',
    responses={200: ItemSerializer}
)
@api_view(['GET'])
def list_view(request):
    list = Items.objects.all()
    serializer = ItemSerializer(list,many=True)#we are taking model data and conveting  to json data

    return Response(serializer.data,status=status.HTTP_200_OK)

@swagger_auto_schema(
    method='get',
    responses={200: ItemSerializer})
@api_view(['GET'])
def detail_view(request,id):
    try:
        item = Items.objects.get(pk=id)
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    except Items.DoesNotExist:
        return Response({'error ':'Item not found'},status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(
    method='put',
    request_body=ItemSerializer
)
@api_view(['PUT'])
def update(request,id):
    try:
        item = Items.objects.get(pk=id)
        serializer = ItemSerializer(item,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'error':'Item does not found'},status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(
    method='delete'
)
@api_view(['DELETE'])
def delete(request,id):
    try:
        item = Items.objects.get(pk=id)
        item.delete()
        return Response({'message':'item deleted'})
    except:
        return Response({'error':'Item does not found'},status=status.HTTP_404_NOT_FOUND)