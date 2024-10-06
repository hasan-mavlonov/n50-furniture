from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse_lazy
from users.form import LoginForm, RegistrationForm


def user_page(request):
    return render(request, 'user-acount.html')


def login_page(request):
    form = LoginForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('homepage'))
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'user-login.html', {'form': form})


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Hash the password and save the user
            user.set_password(form.cleaned_data['password1'])
            user.save()
            # Log the user in after registration
            login(request, user)
            return redirect(reverse_lazy('homepage'))
        else:
            # Form is invalid, render the template with errors
            return render(request, 'user-register.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'user-register.html', {'form': form})
