from rest_framework import serializers
from .models import MaintainenceJobs

class JobsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MaintainenceJobs
        fields = '__all__'