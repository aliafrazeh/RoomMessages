from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# UserAdmin.fieldsets += (
#      (None, {'fields': ('picture')}),
# )

admin.site.register(User, UserAdmin)
