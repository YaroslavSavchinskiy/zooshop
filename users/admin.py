from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'created_at')

    list_filter = ('created_at',)

    search_fields = ('user__username', 'phone_number')

