from django.urls import path
from . import views
urlpatterns = [
    path('',views.contacts_about, name='contacts_about')
]