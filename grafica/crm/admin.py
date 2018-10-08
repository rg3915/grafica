from django.contrib import admin
from .models import UserProfile, PJ, PF


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('first_name', 'last_name', 'email')


@admin.register(PJ)
class PJAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(PF)
class PFAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
