from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from .models import MaintainenceJobs
from .serializer import JobsSerializer
from ships.permission import ISAdminOrEngineer

# Create your views here.
@api_view(['POST'])
@permission_classes([ISAdminOrEngineer])
def jobs_create(request):
    serializer = JobsSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message":"CREATED JOB SUCCESSFULLY!!!"})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def job_list(request):
    jobs = MaintainenceJobs.objects.all()
    serializer = JobsSerializer(jobs, many = True)

    result = []

    for sr in serializer.data:
        result.append({
            "id":sr['id'],
            "ship":sr['ship'],
            "prority":sr['prority'],
            "status":sr['status'],
        })
    return Response(result)

@api_view(['GET'])
def job_details(request,id):
    try:
        job = MaintainenceJobs.objects.get(id=id)
    except MaintainenceJobs.DoesNotExist:
        return Response({"ERROR":"ENTER A VALID ID"},status=status.HTTP_404_NOT_FOUND)
    
    serializer = JobsSerializer(job)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([ISAdminOrEngineer])
def job_update(request,id):
    try:
        job = MaintainenceJobs.objects.get(id=id)
    except MaintainenceJobs.DoesNotExist:
        return Response({"ERROR":"ENTER A VALID ID"},status=status.HTTP_404_NOT_FOUND)
    serializer  = JobsSerializer(job,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([ISAdminOrEngineer])
def job_delete(request,id):
    try:
        job = MaintainenceJobs.objects.get(id=id)
    except MaintainenceJobs.DoesNotExist:
        return Response({"ERROR":"ENTER A VALID ID"},status=status.HTTP_404_NOT_FOUND)
    job.delete()
    return Response({"Message":f"DELETED ({job.ship} where job type is {job.job_type})"})