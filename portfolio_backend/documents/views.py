from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DocumentForm
from portfolio_backend.firestore_utils import create_document, get_document, fetch_all_documents  # Adjust import path

def document_list(request):
    documents = fetch_all_documents()
    if documents:
        return render(request, 'documents/document_list.html', {'documents': documents})
    else:
        return render(request, 'documents/document_list.html', {'empty': True})  # Indicate empty

def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            # Use Firestore interaction  
            create_document(form.cleaned_data['title'], form.cleaned_data['code_content'], form.cleaned_data.get('language'))  
            return redirect('document_list')  
    else:
        form = DocumentForm()
    return render(request, 'documents/document_create.html', {'form': form})

def document_detail(request, document_id):  # Change from 'pk' 
    document_data = get_document(document_id)
    if document_data:
        return render(request, 'documents/document_detail.html', {'document': document_data})
    else:
        # Handle document not found scenario
        pass  # Replace with error handling

def test_firestore(request):
    try:
        # Create a sample document
        create_document("Test Document", "This is a sample code snippet.")

        # Fetch all documents
        documents = fetch_all_documents()
        return HttpResponse(f"Firestore connection successful! Found {len(documents)} documents.") 
    except Exception as e: 
        return HttpResponse(f"Firestore connection error: {str(e)}")