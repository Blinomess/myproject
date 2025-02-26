from django.shortcuts import render

def message_text(request):
    return render(request, 'message/make_a_message.html')

