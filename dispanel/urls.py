from django.urls import path
from .views import login_view, dispatcher_panel, logout_view
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', login_view, name='login'),
    path('panel/', dispatcher_panel, name='dispatcher_panel'),
    path('logout/', logout_view, name='logout')
]