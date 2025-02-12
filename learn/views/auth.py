from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib.auth.models import User, Group
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


def login(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            user_login(request, user)
            print(user)
            return redirect('index')
        else:
            return render(request, "learn/auth/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "learn/auth/login.html") if request.user.is_anonymous else redirect('index')


def forgot_password(request):
    return render(request, "learn/auth/login.html") if request.user.is_anonymous else redirect('index')


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        role = request.POST["role"]
        confirmation = request.POST["confirmation"]
        email = request.POST['email']
        print(role)
        if role not in ("teacher", "student"):
            return render(request, "learn/auth/register.html", {
                "message": "Invalid role"
            })

        if password != confirmation:
            return render(request, "learn/auth/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username=username, password=password, email=email)
            student_group = Group.objects.get(name=role.capitalize())
            user.groups.add(student_group)
            user.save()
        except IntegrityError:
            return render(request, "learn/auth/register.html", {
                "message": "Username already taken."
            })
        user_login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "learn/auth/register.html") if request.user.is_anonymous else redirect('index')


def logout(request):
    user_logout(request)
    return redirect('index')
