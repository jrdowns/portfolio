from django.urls import path
from . import views

urlpatterns = [
    # ... your other URLs ...
    path('test-firestore/', views.test_firestore, name='test_firestore'),
    path('document-list/', views.document_list, name='document_list'),
    path('document-create/', views.document_create, name='document_create'),
    path('document-detail/<str:document_id>/', views.document_detail, name='document_detail'),
]
