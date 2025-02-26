from django.shortcuts import render

def contacts_about(request):
    return render(request, 'contacts/contacts.html')