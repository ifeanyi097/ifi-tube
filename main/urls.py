from django.urls import path
from .views import index, videos

urlpatterns =[
    path('', index, name="inđex"),
    path('videos', videos, name="videos"),
]