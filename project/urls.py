from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cnvd/', include('cnvd.urls')),
    path('api/produtividade/', include('produtividade.urls')),
]
