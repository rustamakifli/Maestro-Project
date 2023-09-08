from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()
# Register your models here.

@admin.register(User)
class MyUserAdmin(UserAdmin):
    readonly_fields = (
        "last_activity",
        "is_from_app",
        "current_sign_in_ip",
        "last_sign_in_ip",
        "sign_in_count",
    )
    fieldsets = (
        (
            ("Personal info"),
            {
                "fields": (
                    "password",
                    "first_name",
                    "last_name",
                    "gender",
                    "image",
                    "email",
                    "last_activity",
                    "is_from_app",
                    "current_sign_in_ip",
                    "last_sign_in_ip",
                    "sign_in_count",
                )
            },
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            ("Important dates"),
            {"fields": ("last_login", "date_joined")},
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    # "username",
                    # "password1",
                    # "password2",
                ),
            },
        ),
    )
    # The forms to add and change user instances
    # form = MyUserChangeForm
    # add_form = MyUserCreationForm
    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "date_joined",
    )
    list_filter = (
        "is_staff",
        "is_superuser",
        "is_active",
        "groups",
        "date_joined",
        "last_activity",
    )
    search_fields = ("first_name", "last_name", "email",  )
    ordering = ("-date_joined",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )