from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()

            messages.success(request, f"Account created for {username}")

            return redirect('index')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
