from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def register_view(request):
    # Check if the form has been submitted
    if request.method == "POST":
        # Instantiate form with submitted data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post:list")  # Redirect to home page
    else:
        # GET request: Instantiate an empty form
        form = UserCreationForm()

    # Return rendered template, passing the form context
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        # Explicitly pass data argument
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Retrieve the authenticated user
            user = form.get_user()
            # Log the user in
            login(request, user)
            return redirect("post:list")
    else:
        # GET request: empty form
        form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
