from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm
from message.models import Messages
from django.http import JsonResponse

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
    active_messages = Messages.objects.filter(status='active').order_by('-created_at')
    completed_messages = Messages.objects.filter(status='completed').order_by('-created_at')
    return render(request, 'dispanel/dispanel_home.html', {
        'active_messages': active_messages,
        'completed_messages': completed_messages
    })
