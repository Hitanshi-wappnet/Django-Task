from django.db import models


# Create your models here.
class UserInformation(models.Model):
    class Meta:
        verbose_name = "User_Information"
        # ordering = [-1]
        # db_table = 'Registration'

    id = models.AutoField(auto_created=True, primary_key=True,
                          verbose_name="ID")
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    mobileno = models.CharField(
        unique=True,
        error_messages={"unique": "The Geeks Field you entered is not unique"},
        help_text="Please enter your mobile number here",
        blank=True,
        default=None,
        max_length=12
    )
    birthdate = models.DateField(
        help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
        blank=True,
        default=None,
    )
    age = models.DecimalField(max_digits=5, decimal_places=0, default=None)
    email = models.EmailField(max_length=254, default=None)
    salary = models.FloatField(blank=True, default=None)
    address = models.TextField(blank=True, default=None)
    review = models.CharField(max_length=300, default=None,
                              help_text="Please upload file on your reviews")
    agree = models.BooleanField(
        help_text="Agree with Terms and conditions", blank=True, default=None
    )
