from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

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