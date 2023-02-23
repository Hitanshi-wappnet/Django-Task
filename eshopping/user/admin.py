from django.contrib import admin
from user.models import UserInformation


# Register your models here.
# Register Model in Django Admin
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
        "age",
        "salary",
        "address",
        "review",
        "agree",
    ]
    search_fields = ("name",)
    list_filter = ["mobileno"]
    fieldsets = (
        ("Personal Information", {"fields": ("name", "birthdate", "age")}),
        (
            "Contact_Information",
            {
                "fields": ("mobileno", "email"),
            },
        ),
    )
    # fields = ["name", "mobileno", "email", "address"]
    # raw_id_fields = ("salary",)

    # Read Only Fields
    readonly_fields = ["mobileno", "email"]
    # date_hierarchy = ["birthdate"]
