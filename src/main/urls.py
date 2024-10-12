
from django.contrib import admin
from django.urls import path, include
#kikuchibranch03
urlpatterns = [
    path('admin/', admin.site.urls),
    path('nippo/', include('nippo.urls')),
    path('detail/', include('nippo.urls')),
]
