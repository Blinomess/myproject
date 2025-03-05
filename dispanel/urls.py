from django.urls import path
from .views import login_view, dispatcher_panel
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', login_view, name='login'),
    path('panel/', dispatcher_panel, name='dispatcher_panel'),
    path('login/', LogoutView.as_view(next_page='login'), name='logout')
]