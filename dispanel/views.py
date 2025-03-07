from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from message.models import Messages

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

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dispatcher_panel(request):
    messages = Messages.objects.order_by('-created_at')
    return render(request, 'dispanel/dispanel_home.html',  {'messages': messages})