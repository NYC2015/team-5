from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.

def createUser(request):
"""CREATES A USER """

"""Get all user input data"""
    username = request.POST["Username"]
    password = request.POST["Password"]
    snapAcc = request.POST["Snap"]

    user = User.objects.create_user(username, None, password)
    user.save()





def login(request):

"""Log in the user"""
    username = request.POST["Username"]

