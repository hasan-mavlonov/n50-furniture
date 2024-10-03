from users.form import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.
def user_page(request):
    return render(request, 'user-acount.html')


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)  # Use email as the username
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('home'))  # Redirect to home after successful login
            else:
                messages.error(request, 'Invalid email or password.')
    else:
        form = LoginForm()
    return render(request, 'user-login.html', {'form': form})


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Create the user object but don't save it yet
            user = form.save(commit=False)
            # Set the email as username (since Django requires username but we aren't showing it)
            user.username = form.cleaned_data['email']
            # Set the password (hashes the password)
            user.set_password(form.cleaned_data['password'])
            # Save the user object
            user.save()
            # Log the user in after registration
            login(request, user)
            return redirect(reverse_lazy('home'))  # Redirect to home after successful registration
        else:
            # Form is invalid, render the template with form errors
            return render(request, 'user-register.html', {'form': form})
    else:
        # If the request is not POST, render the empty form
        form = RegistrationForm()
    return render(request, 'user-register.html', {'form': form})