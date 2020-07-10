from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

User = get_user_model()


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    ordering = ('email',)
    fieldsets = (("User", {"fields":
                    ('email', 'username', 'password', 'user_photo', 'bio',
                     'is_staff', 'is_active')}),)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username',
                       'password1', 'password2'),
        }),)
    list_display = ["id", "email", "username"]
    search_fields = ["email"]
