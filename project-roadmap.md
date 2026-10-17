# Project Roadmap

## Project

AI Student Assistance & Personalized Learning Chatbot

## Goal

Build a working AI-based student assistance system that combines Machine Learning, NLP, Retrieval-Augmented Generation (RAG), an AI language model, backend services and a web interface.

---

# Phase 0 - Project Planning

### Objectives

- Understand the problem.
- Define the target users.
- Define functional requirements.
- Define system architecture.
- Define the project scope.
- Decide the initial technology stack.

### Status

Completed.

---

# Phase 1 - Development Environment

### Tasks

- Install Python.
- Install VS Code.
- Install required VS Code extensions.
- Create a Python virtual environment.
- Configure Git.
- Create the project repository.
- Create the project folder structure.

### Status

Completed.

---

# Phase 2 - Python Foundations

### Objectives

Learn the Python concepts required for the project.

### Topics

- Variables
- Data types
- Conditions
- Loops
- Functions
- Lists
- Dictionaries
- Strings
- File handling
- Modules
- Exceptions
- Classes and objects
- Working with CSV and JSON data

### Goal

Be able to write and understand the Python code used in the project.

---

# Phase 3 - Machine Learning Foundations

### Objectives

Understand the basic Machine Learning concepts required for text classification.

### Topics

- What is Machine Learning?
- Supervised learning
- Training data
- Features
- Labels
- Training and testing
- Classification
- Model evaluation

### Initial Model

The first intent-classification model will use:

- TF-IDF for text feature extraction.
- Logistic Regression for classification.

The model may be compared with other suitable classification approaches later.

---

# Phase 4 - Student Question Dataset

### Tasks

- Define question categories.
- Create labelled student questions.
- Store questions in a structured dataset.
- Split the dataset into training and testing data.
- Check data quality.
- Remove duplicate or unsuitable examples.

### Initial Intents

- exam_schedule
- attendance
- course_information
- academic_concept
- study_material
- university_policy

---

# Phase 5 - First ML Model

### Tasks

1. Load the question dataset.
2. Preprocess the text.
3. Convert text into numerical features.
4. Train the classifier.
5. Test the classifier.
6. Calculate evaluation metrics.
7. Analyze incorrect predictions.
8. Improve the dataset/model if necessary.

### Evaluation

- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix

---

# Phase 6 - NLP Processing

### Tasks

- Understand text preprocessing.
- Normalize questions.
- Explore tokenization.
- Explore stop-word handling.
- Understand text representation.
- Improve question classification.

---

# Phase 7 - University Knowledge Base

### Tasks

Collect suitable university information such as:

- Syllabus
- Regulations
- Notices
- FAQs
- Academic policies

### Processing Pipeline

Documents
→ Text extraction
→ Cleaning
→ Chunking
→ Embeddings
→ Vector storage

---

# Phase 8 - RAG System

### Tasks

- Understand Retrieval-Augmented Generation.
- Generate document embeddings.
- Store embeddings.
- Perform semantic search.
- Retrieve relevant document chunks.
- Test retrieval quality.
- Handle questions for which information is unavailable.

---

# Phase 9 - AI Language Model

### Tasks

- Connect the retrieved context to an AI language model.
- Create prompts for grounded answers.
- Prevent unsupported answers.
- Return source information with the response.
- Test answer quality.

---

# Phase 10 - Backend

### Technology

FastAPI

### Tasks

- Create backend application.
- Create API endpoint for questions.
- Receive questions from frontend.
- Run classification.
- Perform retrieval.
- Generate response.
- Return answer and sources.

---

# Phase 11 - Frontend

### Initial Technology

- HTML
- CSS
- JavaScript

### Tasks

- Create chatbot interface.
- Add question input.
- Add send button.
- Display responses.
- Display sources.
- Handle loading and error states.

---

# Phase 12 - System Integration

### Tasks

Connect:

Frontend
→ Backend
→ ML Classifier
→ RAG
→ AI Language Model
→ Backend
→ Frontend

### Goal

Create one complete working system.

---

# Phase 13 - Testing and Evaluation

### Tasks

- Test different question types.
- Test incorrect questions.
- Test unknown questions.
- Test retrieval quality.
- Test answer quality.
- Test source display.
- Test system response time.
- Record failure cases.

### Goal

Measure the actual performance of the completed system.

---

# Phase 14 - Deployment

### Tasks

- Prepare production configuration.
- Configure environment variables.
- Deploy backend.
- Deploy frontend.
- Test the deployed application.

---

# Phase 15 - Documentation and Presentation

### Tasks

- Complete README.
- Document architecture.
- Document dataset.
- Document ML methodology.
- Document RAG pipeline.
- Document evaluation results.
- Prepare project presentation.
- Prepare project demonstration.
- Prepare resume/project description.

---

# Development Principle

The project will be developed incrementally.

Each major component will first be understood conceptually, then implemented, tested and integrated.

The project will avoid blindly copying large amounts of AI-generated code.