
# Create your views here.
from pyexpat.errors import messages

from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import RegisterForm


def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(request, "You have been registered successfully!")

            return redirect('home')

    else:

        form = RegisterForm()

    return render(
        request,
        'users/register.html',
        {'form': form}
    
    )