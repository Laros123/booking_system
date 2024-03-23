from django.shortcuts import render, redirect
from auth_system.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from booking_sys.language import get_list_language
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('index')
        else:
            messages.error(request, 'Registration error')
    else:
        form = CustomUserCreationForm()
        return render(
            request,
            'auth_system/register.html',
            context={'form': form, 'language': get_list_language(request.session.get('language'))}
            )

def login_user(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'Wrong login or password')
    else: 
        form = CustomAuthenticationForm()

        return render(
            request, 
            'auth_system/login.html',
            context={'form': form, 'language': get_list_language(request.session.get('language'))}
            )


def logout_user(request):
    logout(request)
    return redirect('register')

@login_required
def profile(request):
    return render(request, 'auth_system/profile.html', {'language': get_list_language(request.session.get('language'))})

def ukrainian(request):
    request.session['language'] = 'ukrainian'
    return redirect('/')

def english(request):
    request.session['language'] = 'english'
    return redirect('/')