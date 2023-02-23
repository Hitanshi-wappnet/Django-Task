from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello This is shopping Website",
                        content_type="text/plain")


def welcome(request):
    return HttpResponse(
        "<h1><center>Welcome to the eshopping website</center></h1>"
        )


# Create your views here.
