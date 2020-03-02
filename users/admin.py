from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    # list_display = ("username", "gender", "language", "currency", "superhost")
    # list_filter = (
    #     "language",
    #     "currency",
    #     "superhost",
    # )


# (줄)5, 6 서로 붙어있어야 사용가능
# models.User의 모델을 admin.register에서 사용할거야 라는 뜻
# 그리고 이class는 CustomUserAdmin이야 라는 뜻

# admin.site.register(models.User, CustomUserAdmin)
# 위 아래 서로 동일한 뜻
# @admin.register(models.User)
# class CustomUserAdmin(admin.ModelAdmin):
#     pass
