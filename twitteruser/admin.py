from django.contrib import admin
from twitteruser.models import CustomUser
from django.contrib.auth.admin import UserAdmin


# From https://stackoverflow.com/questions/48011275/custom-user-model-fields-abstractuser-not-showing-in-django-admin
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,        # original form fieldsets, expanded
        (                            # new fieldset added on to the bottom
            'Custom Field Heading',  # group heading of your choice
            {
                'fields': (
                    'following',
                ),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
