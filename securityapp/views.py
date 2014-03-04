from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from securityapp.forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['username'],
                form.cleaned_data['email'],
                form.cleaned_data['password'],
            )
    else:
        form = SignupForm()
    data = {'form': form}
    return render(request, 'signup.html', data)


