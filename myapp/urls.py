from django.urls import path
from .views import greeting_view

urlpatterns = [
    path('', greeting_view, name='greeting_api'),  # Use as_view() for class-based view
]
