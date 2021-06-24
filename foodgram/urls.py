from django.conf import settings

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('api/', include('api.urls')),
    path('', include('web.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)    
    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)    