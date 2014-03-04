from django.shortcuts import render, redirect

from securityapp.forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect("/signup")
    else:
        form = SignupForm()
    data = {'form': form}
    return render(request, 'signup.html', data)


