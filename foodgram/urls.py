from django.conf import settings
from django.conf.urls import handler404, handler500

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('api/', include('api.urls')),
    path('', include('web.urls')),
]

handler404 = 'web.views.page_not_found'
handler500 = 'web.views.server_error'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)    
    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)

