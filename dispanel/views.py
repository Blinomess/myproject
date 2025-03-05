from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import LoginForm

def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dispatcher_panel') 
    else:
        form = LoginForm()

    return render(request, 'dispanel/login.html', {'form': form})

@login_required
def dispatcher_panel(request):
    return render(request, 'dispanel/dispanel_home.html')