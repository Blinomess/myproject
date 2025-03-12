from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('panel/', views.dispatcher_panel, name='dispatcher_panel'),
    path('logout/', views.logout_view, name='logout'),
    path('<int:pk>/', views.PanelDisplay.as_view(), name='message_details'),
    path('<int:pk>/delete', views.MessageDelete.as_view(), name='message_delete')
]