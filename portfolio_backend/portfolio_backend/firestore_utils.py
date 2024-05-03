# May move this later
import firebase_admin
from firebase_admin import credentials, firestore

# Firebase initialization
cred = credentials.Certificate(r'C:\Users\jdown\Documents\portfolio-422119-38cb808fb141.json')
firebase_admin.initialize_app(cred)
db = firestore.client()  # Access to Firestore

documents_ref = db.collection('documents')  # Reference to your 'documents' collection

def create_document(title, code_content, language=None):
    document_data = {
        'title': title,
        'code_content': code_content,
        'language': language,  # Optional field
        'created_at': firestore.SERVER_TIMESTAMP, 
        'updated_at': firestore.SERVER_TIMESTAMP,
    }
    doc_ref = documents_ref.add(document_data)
    return doc_ref  # The automatically generated ID

def get_document(document_id):
    doc_ref = documents_ref.document(document_id)
    return doc_ref.get().to_dict()  # Returns a dictionary if found

def fetch_all_documents():
    documents = []
    for doc in documents_ref.stream():
        document_data = doc.to_dict()
        document_data['id'] = doc.id  # Assign the ID explicitly
        documents.append(document_data)
    return documents

def create_comment(document_id, line_number, text, author=None):
    comment_data = {
        'lineNumber': line_number,
        'text': text,
        'createdAt': firestore.SERVER_TIMESTAMP
    }
    if author:
        comment_data['author'] = author  

    doc_ref = documents_ref.document(document_id)
    comment_ref = doc_ref.collection('comments').add(comment_data)
    return comment_ref.id  # Return the comment ID for potential use

def get_comments(document_id):
    doc_ref = documents_ref.document(document_id)
    return doc_ref.collection('comments').order_by('lineNumber').stream() 
