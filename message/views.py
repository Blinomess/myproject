from django.shortcuts import render
from .forms import MessagesForm

def message_text(request):
    error=''
    if request.method=='POST':
        form=MessagesForm(request.POST)
        if form.is_valid():
            form.save()
            #добавить высвечивание сообщения о успешной отправке сообщения или см в.9 21:00
        else:
            error='Сообщение было написано неверно'

    form= MessagesForm()

    data={
        'form': form,
        'error': error
    }

    return render(request, 'message/make_a_message.html',data)