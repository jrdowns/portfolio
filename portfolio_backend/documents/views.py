from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm  # Create this form later

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'documents/document_list.html', {'documents': documents})

def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('document_list')  # Name your list view accordingly
    else:
        form = DocumentForm()
    return render(request, 'documents/document_create.html', {'form': form})

def document_detail(request, pk):
    document = Document.objects.get(pk=pk)
    return render(request, 'documents/document_detail.html', {'document': document})
