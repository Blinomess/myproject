from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.message_text, name='create'),
]