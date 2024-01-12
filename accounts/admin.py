from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdminCustom(UserAdmin):
    # detail
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "uid",
                    "name",
                    "email",
                    "password",
                    "avatar",
                    "introduction",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "updated_at",
                    "created_at",
                )
            },
        ),
    )

    #addition
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )

    #list
    list_display = (
        "uid",
        "name",
        "email",
        "is_active",
        "updated_at",
        "created_at",
    )

    list_filter = ()
    #search
    search_fields = (
        "uid",
        "email",
    )
    #order
    ordering = ("updated_at",)
    #link
    list_display_links = ("uid", "name", "email")
    #readonly
    readonly_fields = ("updated_at", "created_at", "uid")


admin.site.register(User, UserAdminCustom)