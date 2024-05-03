# Project Title: Code Snippet Sharing and Commenting Platform  

## Description  

This web application built with Django and Firestore enables users to:  

Create and store code snippets with optional language specification.  
View a list of all shared code snippets.  
View details of individual code snippets with syntax highlighting (using Prism.js).  
Leave comments on specific lines of code within a snippet.  

## Technologies  

Backend: 
  - Django (Python web framework)  
Database:
  - Firestore (NoSQL Database from Google Cloud)  
Frontend:  
  - Django Templating  
  - Prism.js (for code syntax highlighting)  
  - Vanilla JavaScript (for minimal frontend interactivity)  

## Getting Started  

### 1. Prerequisites:  
  - Python 3.x  
  - Node.js (to install npm packages)  
  - Google Cloud Project with a Firestore database  
### 2. Setup  
  - Clone the repository: git clone https://github.com/jrdowns/portfolio.git  
  - Install dependencies: pip install -r requirements.txt  
  - Set up the Firebase configuration in firestore_utils.py with your project credentials.  
### 3. Run the Development Server  
  - python manage.py runserver

## How to Use  

  - Visit http://127.0.0.1:8000/ to access the application.  
  - Create a new code snippet.  
  - Explore the list of existing snippets.  
  - Click on a snippet to view its details and add line-specific comments.
    
## Future Development

  - Implement user authentication to associate comments with users.  
  - Explore using React for a richer, more interactive frontend experience.  
  - Add search and filtering capability to find snippets.
  - Add live chat
    
Note: This project uses the Firebase Emulator. Ensure you have it installed and running for local development.  
