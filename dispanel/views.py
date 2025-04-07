from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from .forms import LoginForm
from message.models import Messages
from django.views.generic import DetailView, DeleteView

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
    new_messages =Messages.objects.filter(status='new').order_by('-created_at')
    read_messages = Messages.objects.filter(status='read').order_by('-created_at')
    return render(request, 'dispanel/dispanel_home.html',  {
        'new_messages': new_messages,
        'read_messages': read_messages
    })

class PanelDisplay (DetailView):
    model=Messages
    template_name='dispanel/message_display.html'
    context_object_name='message'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        message = context['message']

        if message.status=='new':
            message.status='read'
            message.save()

        new_messages =Messages.objects.filter(status='new').order_by('-created_at')
        read_messages = Messages.objects.filter(status='read').order_by('-created_at')
        context['new_messages'] = new_messages
        context['read_messages'] = read_messages
        return context
    
class MessageDelete (DeleteView):
    model=Messages
    template_name='dispanel/delete.html'
    context_object_name = 'message'
    success_url = reverse_lazy('dispatcher_panel')
