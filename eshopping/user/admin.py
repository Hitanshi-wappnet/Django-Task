from django.contrib import admin
from user.models import UserInformation


# Register your models here.
@admin.register(UserInformation)
class UserInformationAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "created_at",
        "updated_at",
        "mobileno",
        "birthdate",
        "email",
        "salary",
        "address",
        "review",
        "agree",
    ]
