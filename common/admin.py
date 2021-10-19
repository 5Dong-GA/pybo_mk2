from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['profile_name', 'bio']


admin.site.register(Profile, ProfileAdmin)