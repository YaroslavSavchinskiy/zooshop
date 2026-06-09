from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('goods:home')
    else:
        form = RegisterForm()

    register_data = {
        'form': form,
    }

    return render(request, 'users/register.html', register_data)

@login_required
def profile_view(request):
    profile = request.user.profile

    profile_data = {
        'profile': profile,
    }

    return render(request, 'users/profile.html', profile_data)

@login_required
def profile_edit_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('users:profile')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'users/profile_edit.html', {'form': form})