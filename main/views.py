from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Проверка</h1>")

def about(request):
    return HttpResponse("<h1>КАКИЕ КОНТАКТЫ Я ЧЁ ПОХОЖ НА ОБОНЕНТА</h1>")