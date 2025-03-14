from django.shortcuts import render, redirect
from .forms import MessagesForm
from .models import Location

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

def map_view(request):
    if request.method == "POST":
        lat = request.POST.get("latitude")
        lng = request.POST.get("longitude")
        if lat and lng:
            Location.objects.create(latitude=lat, longitude=lng)
            return redirect("success_page")  # Перенаправляем на страницу успеха
    return render(request, "map.html")