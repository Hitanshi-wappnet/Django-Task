from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    user_list = {"Shreya", "Khyati", "Shivam", "Prish"}
    return render(request, "home.html", context={"data": user_list})


def welcome(request):
    return HttpResponse("<h1><center>Welcome to the eshopping website</center></h1>")
