# AI Student Assistance Chatbot

## 1. Problem Statement

Students frequently need information about examinations, academic policies, courses, study resources, attendance, results, and other university-related matters.

This information is often distributed across different documents, notices, regulations, websites, and academic resources. Students may have difficulty finding the correct information quickly and may receive incomplete or unreliable answers from general-purpose search or conversational systems.

Therefore, there is a need for an AI-based student assistance system that can understand student questions and provide reliable, relevant, and source-grounded answers from university-specific information.

## 2. Proposed Solution

The proposed system is an AI Student Assistance Chatbot that uses Natural Language Processing, Machine Learning, Retrieval-Augmented Generation (RAG), and a Large Language Model (LLM).

The system will:

1. Accept a student's question through a chatbot interface.
2. Process and classify the question into an appropriate intent.
3. Search the university knowledge base for relevant information.
4. Provide the retrieved information as context to the language model.
5. Generate a clear answer based on the retrieved information.
6. Display the answer along with its source whenever possible.
7. Handle questions for which relevant information cannot be found.

## 3. Target Users

The primary users of the system are university students.

The system may support questions related to:

- Examination schedules
- Examination results
- Attendance
- Course information
- Academic concepts
- Study materials
- University policies and regulations

## 4. Objectives

The main objectives are:

- Build a functional AI-based student assistance chatbot.
- Develop a supervised ML model for student-question intent classification.
- Build a university-specific knowledge base.
- Implement semantic retrieval using a RAG pipeline.
- Generate source-grounded answers using an LLM.
- Display relevant sources with answers.
- Evaluate the performance of the intent classifier and retrieval system.
- Reduce incorrect or unsupported answers.

## 5. Expected Outcome

The final system should allow a student to enter a natural-language academic question and receive a relevant answer based on the available university knowledge base.

The system should also identify questions that cannot be answered reliably instead of generating unsupported information.