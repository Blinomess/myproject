from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('contacts/', include('contacts.urls')),
    path('dispanel/',include('dispanel.urls')),
    path('messages/',include('message.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
