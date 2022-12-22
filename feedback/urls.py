from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from apps.accounts import urls as accounts_urls
from apps.comments import urls as comments_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(accounts_urls, namespace='accounts')),
    path('comments/', include(comments_urls, namespace='comments')),
    path('', include('apps.home.urls', namespace='home')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
