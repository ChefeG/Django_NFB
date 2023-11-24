from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'), name='main'),
    path('accounts/', include('allauth.urls'), name='account'),

    path('pages/', include('django.contrib.flatpages.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('contact/', include('contact.urls')),
    path('i18n/', include('django.conf.urls.i18n')),

]

urlpatterns += i18n_patterns(
    path('', include('movies.urls')),
    path('contact/', include('contact.urls')),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


