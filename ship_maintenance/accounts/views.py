from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.authtoken.models  import Token

from .serializer import ProfileSerializer,RegisterUserSerializer,LoginSerializer
from .models import Profile
from django.contrib.auth.models import User

@api_view(['POST'])
def user_register(request):
    serializer = RegisterUserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        return Response({
            "message":'Registered User successfully',
            "user_id":user.id,
            "username": user.username,
            "email":user.email,
        },status = status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
@api_view(['POST'])
def user_login(request):
    serializer = LoginSerializer(data=request.data)

    if not serializer.is_valid():
        return Response({'error':"ENTER CORRECT EMAIL AND PASSWORD"},status=status.HTTP_400_BAD_REQUEST)
    
    user = serializer.validated_data['user']
    token, _ = Token.objects.get_or_create(user=user)
    profile = Profile.objects.filter(user=user).first()
    return Response({
        "token": token.key,
        "user_id" :  user.id,
        "email":user.email,
        "role":profile.role if profile else None,
    },status=status.HTTP_200_OK)


def is_admin(user):
    if not user.is_authenticated:
        return False
    profile = Profile.objects.filter(user=user).first()
    if not profile:
        return False

    return profile.role == 'admin'
    
@api_view(['GET'])
def users_list(request):

    # check login
    if not request.user.is_authenticated:
        return Response(
            {"error": "Login required"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    # check admin role
    if not is_admin(request.user):
        return Response(
            {"error": "Only admin can view users"},
            status=status.HTTP_403_FORBIDDEN
        )

    users = User.objects.all()
    result = []

    for user in users:
        profile = Profile.objects.filter(user=user).first()

        result.append({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": profile.role if profile else None
        })

    return Response(result, status=status.HTTP_200_OK)



@api_view(['GET'])
def user_detail(request,id):
    if not is_admin(request.user):
        return Response({"error": "Only ADMIN can view users"}, status=status.HTTP_403_FORBIDDEN)
    
    try:
        user = User.objects.get(id=id)
    except:
        return Response({"error":'USER DOES NOTEXISTS'},status=status.HTTP_404_NOT_FOUND)

    profile = Profile.objects.filter(user=user)
    return Response({
        "id": user.id,
        "username": user.username, 
        "email": user.email,
        "role": profile.role if profile else None,
        "phone_no":profile.phone_no if profile else None ,
        "address":profile.address if profile else None
    },status= status.HTTP_200_OK)

@api_view(['PUT'])
def user_update(request,id):
    if not is_admin(request.user):
        return Response({"error": "Only ADMIN can update users"}, status=status.HTTP_403_FORBIDDEN)

    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    profile =Profile.objects.filter(user=user).first()
    #update user
    user.username = request.data.get('username',user.username)
    user.email = request.data.get('email',user.email)
    user.save()
    if profile:
        profile.role = request.data.get('role', profile.role)
        profile.phone_no = request.data.get('phone_no', profile.phone_no)
        profile.address = request.data.get('address', profile.address)
        profile.save()

    return Response({"message": "User updated successfully"}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def user_delete(request,id):
    if not is_admin(request.user):
        return Response({'ERROR':"ONLY ADMIN CAN REMOVE"},status=status.HTTP_401_UNAUTHORIZED)
    try:
        user = User.objects .get(id=id)
    except:
        return Response({'ERROR':"User not found"},status=status.HTTP_404_NOT_FOUND)
    
    user.delete()

    return Response({'message':'DELETED USER SUCCESSFULLY'},status=status.HTTP_200_OK)