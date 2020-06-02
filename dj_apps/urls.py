from django.urls import path
from .views import create_app


urlpatterns = [
    path('create/', create_app, name='create_app')
]
