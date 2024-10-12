from django.urls import path
from .views import nippoDetailView, nippoListlView

urlpatterns = [
    path('detail/', nippoDetailView),
    path('', nippoListlView),
]
