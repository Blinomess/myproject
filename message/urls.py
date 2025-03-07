from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.message_text, name='create'),
    path('message_complete/',views.message_complete, name='message_complete')
]