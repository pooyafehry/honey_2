# user/views.py
from datetime import timedelta

from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .forms import UserRegisterForm, AddressForm
from categorylist.forms import CommentForm

def home_page(request):
    return render(request, 'HomePage.html')  # Template name and location

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful')
            return redirect('test')  # Ensure this URL pattern exists
        else:
            messages.error(request, 'Registration failed. Please try again.')
    else:
        form = UserRegisterForm()
    
    context = {'form': form}
    return render(request, 'UserRegister.html', context)

@csrf_exempt
def test_view(request):
    return render(request, 'test.html')  # Template name and location

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful')
                return redirect('home_page')  # Redirect to home page after successful login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

@login_required
def continue_shopping(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('home_page')  # Redirect to the home page or any other page after saving the address
    else:
        form = AddressForm()

    return render(request, 'continue_shopping.html', {'form': form})
