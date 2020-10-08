from django.contrib import admin
from twitteruser.models import CustomUser
from django.contrib.auth.admin import UserAdmin


'''From https://stackoverflow.com/questions/48011275/custom-user-model-fields-
abstractuser-not-showing-in-django-admin'''


class CustomUserAdmin(UserAdmin):
    fieldsets = (*UserAdmin.fieldsets, (None, {
        "fields": (
            'full_name',
            'following',
            'profile_pic',
        ),
    },),
    )


admin.site.register(CustomUser, CustomUserAdmin)
