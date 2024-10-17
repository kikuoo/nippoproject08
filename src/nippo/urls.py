from django.urls import path
from .views import nippoDetailView, nippoListView

urlpatterns = [
    path('nippo/', nippoListView),
    path('detail/<int:number>/', nippoDetailView),
]
