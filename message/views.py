from django.shortcuts import render, redirect
from .forms import MessagesForm
from .models import Messages

def message_text(request):
    if request.method=='POST':
        form=MessagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message_complete')
    else:   
        form = MessagesForm()
    return render(request, 'message\make_a_message.html', {'form': form})

def message_complete(request):
    return render(request, 'message\message_complete.html')