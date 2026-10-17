# AI Student Assistance & Personalized Learning Chatbot

An AI-based student assistance system designed to help students obtain reliable answers to academic and institutional questions.

## 1. Project Overview

Students often need information about examinations, attendance, courses, university policies, regulations, notices and study-related topics.

This project aims to develop a chatbot that can retrieve relevant information from a university knowledge base and provide source-grounded answers.

The system combines:

- Machine Learning
- Natural Language Processing
- Retrieval-Augmented Generation (RAG)
- AI Language Models
- Backend APIs
- Web Technologies

## 2. Problem

Academic and institutional information may be distributed across multiple documents and sources.

Students may spend significant time searching for the correct information manually.

A chatbot that retrieves information from a university knowledge base can provide a more convenient way for students to access supported information.

## 3. Proposed Solution

The proposed system allows a student to enter a question through a web interface.

The system will:

1. Receive the student's question.
2. Classify the question into an appropriate intent.
3. Search the university knowledge base.
4. Retrieve relevant information.
5. Generate an answer using the retrieved information.
6. Display the answer and its source.
7. Indicate when the required information cannot be found.

## 4. Main Technologies

### Machine Learning

The project will use supervised Machine Learning for student-question intent classification.

Initial approach:

- TF-IDF
- Logistic Regression

### NLP

Natural Language Processing will be used to process and represent student questions.

### RAG

Retrieval-Augmented Generation will be used to retrieve relevant information from university documents before generating an answer.

### Backend

The planned backend framework is:

- FastAPI

### Frontend

The initial frontend will use:

- HTML
- CSS
- JavaScript

### Version Control

- Git
- GitHub

## 5. Initial Question Intents

The first version of the classifier will include:

- `exam_schedule`
- `attendance`
- `course_information`
- `academic_concept`
- `study_material`
- `university_policy`

These categories may be expanded as the project develops.

## 6. Knowledge Base

The planned knowledge base may contain:

- Syllabus documents
- Academic regulations
- University notices
- FAQs
- Academic policies

## 7. System Architecture

```text
Student
   |
   v
Web Interface
   |
   v
Backend API
   |
   v
Question Processing
   |
   v
ML Intent Classifier
   |
   v
RAG Retrieval
   |
   v
University Knowledge Base
   |
   v
AI Language Model
   |
   v
Answer + Source
   |
   v
Student