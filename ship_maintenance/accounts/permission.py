from rest_framework.permissions import BasePermission
from .models import Profile

class RoleBasedUSerPermission(BasePermission):
    def has_permission(self,request,view):

            # Runs before the view executes
            # Decides whether the request should proceed
            # Must return:
            # True → Allow request
            # False → Deny request (403)

        #user must be login
        if not request.user.is_authenticated:
            return False
        
        try:
            profile = Profile.objects.filter(user=request.user).first()
        except Profile.DoesNotExist:
            return False
        
        # allow all roles to view users
        if request.method =='GET':
            return True
        
        # allow only admin to Do CRUD operations
        if profile =='ADMIN':
            return True
        
        return False