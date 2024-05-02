from django.shortcuts import render, redirect
from .forms import DocumentForm
from portfolio_backend.firestore_utils import create_document, get_document, fetch_all_documents  # Adjust import path

def document_list(request):
    # We'll need to adapt how we fetch documents for Firestore
    documents_data = fetch_all_documents()
    return render(request, 'documents/document_list.html', {'documents': documents_data})

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
