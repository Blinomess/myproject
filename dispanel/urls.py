from django.urls import path
from .views import login_view, dispatcher_panel
from . import views
urlpatterns = [
    path('login/', login_view, name='login'),
    path('panel/', dispatcher_panel, name='dispatcher_panel')
]