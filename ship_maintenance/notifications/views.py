from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from .models import Notification
from.serializer import NotificationsSerializer
from ships.permission import ISAdminOrEngineer

# Create your views here.
@api_view(['POST'])
@permission_classes([ISAdminOrEngineer])
def notification_create(request):

    serializer = NotificationsSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(['GET'])
def notification_list(request):

    notifications = Notification.objects.filter(user=request.user)
    serializer = NotificationsSerializer(notifications, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def all_notifications(request):
    notification = Notification.objects.all()
    serializer = NotificationsSerializer(notification,many = True)

    return Response(serializer.data)


@api_view(['PUT'])
def mark_as_read(request, id):

    try:
        notification = Notification.objects.get(id=id, user=request.user)
    except Notification.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    notification.is_read = True
    notification.save()

    return Response({"message": "Marked as read"})

@api_view(['DELETE'])
@permission_classes([ISAdminOrEngineer])
def notification_delete(request, id):

    try:
        notification = Notification.objects.get(id=id, user=request.user)
    except Notification.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    notification.delete()

    return Response({"message": "Deleted"})