# System Architecture

## 1. Overview

The AI Student Assistance Chatbot is designed as a Python-based application using Streamlit for the user interface and Python-based Machine Learning, Natural Language Processing, Retrieval-Augmented Generation (RAG), and LLM components.

The system follows the pipeline:

Student
↓
Streamlit Chat Interface
↓
Question Processing
↓
ML Intent Classifier
↓
Knowledge Retrieval
↓
University Knowledge Base
↓
LLM
↓
Answer + Source
↓
Student

## 2. High-Level Architecture

```text
┌─────────────────────────────┐
│          Student            │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│     Streamlit Interface     │
│      Chatbot Interface      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    Question Processing      │
│ Cleaning / Normalization    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│    ML Intent Classifier     │
│   TF-IDF + Logistic Reg.    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│       RAG Retrieval         │
│ Semantic Search / Retrieval │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ University Knowledge Base   │
│ PDFs / FAQs / Policies /   │
│ Notices / Syllabus / etc.  │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│            LLM              │
│     Answer Generation       │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│      Answer + Source        │
└─────────────────────────────┘