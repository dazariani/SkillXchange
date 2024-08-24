from django.contrib import admin
from .models import CustomUser, SkillClass, Enrollment, Review
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
  model = CustomUser
  add_form = CustomUserCreationForm

  fieldsets = (
    *UserAdmin.fieldsets,
    (
      'User role',
      {
        'fields': (
          'isTutor',
          'isStudent',
        )
      }
    )
  )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SkillClass)
admin.site.register(Enrollment)
admin.site.register(Review)