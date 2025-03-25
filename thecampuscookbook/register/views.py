from django.shortcuts import render
from register.forms import UserForm, UserProfileForm

# Create your views here.


def register(request):
    # Used by template to check if user is registered
    registered = False

    # Process form if it's a POST request
    if request.method == "POST":
        # Get information from raw POST request
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Set commit=False since user field within profile_form must be set.
            profile = profile_form.save(commit=False)
            profile.user = user

            if "avatar" in request.FILES:
                profile.avatar = request.FILES["avatar"]

            profile.save()

            # Updated variable to indicate that the template registration was successful
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        # Show blank forms if it's a GET request
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(
        request,
        "register/register.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
            "registered": registered,
        },
    )
