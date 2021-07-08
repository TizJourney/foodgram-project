from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    list_filter = ('email', 'username')


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
