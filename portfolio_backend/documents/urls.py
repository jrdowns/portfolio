from django.urls import path
from . import views

urlpatterns = [
    # ... your other URLs ...
    path('test-firestore/', views.test_firestore, name='test_firestore'),
]
