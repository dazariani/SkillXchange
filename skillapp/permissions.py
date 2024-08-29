from rest_framework import permissions
from .models import Enrollment, SkillClass


# Skill class permissions
class SkillClassPermissionObjLevel(permissions.BasePermission):

  def has_object_permission(self, request, view, obj):

    if request.method in permissions.SAFE_METHODS:
      return True
    if request.user.is_staff:
      return True
    
    return obj.tutor.id == request.user.id
  
  
class SkillClassPermissionModelLevel(permissions.BasePermission):

  def has_permission(self, request, view):

    if (request.method == 'POST' and request.user.isTutor == False and request.user.is_staff == False):
      return False
    return True


# Enrollment permissions
class EnrollmentPermissionObjLevel(permissions.BasePermission):

  def has_object_permission(self, request, view, obj):

    if request.user.is_staff:
      return True
    
    return obj.student.id == request.user.id
  

class EnrollmentPermissionModelLevel(permissions.BasePermission):
  message = ''

  def has_permission(self, request, view):
    currentEnrollments = Enrollment.objects.filter(skillClass=request.data.get('skillClass'))
    maxStudentCount = SkillClass.objects.get(id=request.data.get('skillClass')).maxStudents
    

    if (view.action == 'list' and request.user.is_staff == False) or (request.method == 'POST' and request.user.isStudent == False and request.user.is_staff == False):
      self.message = 'You do not have permission to perform this action.'
      return False 
    
    if len(currentEnrollments) >= (maxStudentCount):
      self.message = 'No more places available right now :('
      return False
    
    return True
  

# Reviews permissions
class ReviewPermissionObjLevel(permissions.BasePermission):

  def has_object_permission(self, request, view, obj):

    if request.user.is_staff:
      return True
    
    return obj.client.id == request.user.id
  

class ReviewPermissionModelLevel(permissions.BasePermission):

  def has_permission(self, request, view):

    if (view.action == 'list' and request.user.is_staff == False) or (request.method == 'POST' and request.user.isStudent == False and request.user.is_staff == False):
      return False 
    
    return True
  


