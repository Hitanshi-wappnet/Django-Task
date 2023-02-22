from django.db import models


# Create your models here.
class UserInformation(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True,
                          verbose_name="ID")
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mobileno = models.IntegerField(
        unique=True,
        error_messages={"unique": "The Geeks Field you entered is not unique."},
        blank=True
    )
    birthdate = models.DateField(
        help_text="Please use the following format: <em>DD-MM-YYYY</em>.",
        blank=True
    )
    email = models.EmailField(max_length=254)
    salary = models.FloatField(blank=True)
    address = models.TextField(blank=True)
    review = models.FileField(upload_to=None, max_length=254)
    agree = models.BooleanField(help_text="Agree with Terms and conditions", blank=True)
