from django.shortcuts import render, redirect
from .forms import MessagesForm

def message_text(request):
    if request.method=='POST':
        form=MessagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:   
        form = MessagesForm()
    return render(request, 'message\make_a_message.html', {'form': form})

