# from django.views.generic import RedirectView
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Tender.urls')),
    path('tender/', include('Tender.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
