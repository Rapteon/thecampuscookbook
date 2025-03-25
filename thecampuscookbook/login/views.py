from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def user_login(request):
    # If user is trying to login.
    if request.method == "POST":
        # Get information from POST request sent by login form.
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Authenticate the user.
        user = authenticate(request=request, username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                # Redirect to home page.
                return redirect("home")
            else:
                return HttpResponse("Your account is disabled.")
        else:
            # Invalid login details.
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")

    else:
        # Display blank login form.
        return render(request, "login/login.html")


# User must be logged in to log out.
@login_required
def user_logout(request):
    logout(request)
    # Redirect to home page on logout.
    return redirect("home")


def user_restricted(request):
    return render(request, "login/restricted.html")
