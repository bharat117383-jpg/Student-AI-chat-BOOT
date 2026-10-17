# System Requirements

## 1. Problem Statement

Students need reliable answers to academic and institutional
queries. Relevant information may be distributed across
syllabi, regulations, notices, FAQs and academic policies.

The proposed system is an AI Student Assistance Chatbot that
retrieves relevant information from a university knowledge base
and provides source-grounded answers.

## 2. Target Users

- Students

## 3. Functional Requirements

### FR1 - Question Input
The student should be able to enter a question.

### FR2 - Question Classification
The system should classify the student's question into an
appropriate intent.

### FR3 - Knowledge Retrieval
The system should retrieve relevant information from the
university knowledge base.

### FR4 - Answer Generation
The system should generate a natural-language answer based
on the retrieved information.

### FR5 - Source Display
The system should display the source of the retrieved
information.

### FR6 - Unknown Questions
The system should indicate when the required information
cannot be found in the available knowledge base.

## 4. Machine Learning Requirements

The system will include a supervised machine-learning model
for student-question intent classification.

Initial intents:

- exam_schedule
- attendance
- course_information
- academic_concept
- study_material
- university_policy

The model will be trained and evaluated using a labelled
student-question dataset.

## 5. RAG Requirements

The system should use a university knowledge corpus containing
relevant academic and institutional information.

Potential sources include:

- Syllabus
- Regulations
- Notices
- FAQs
- Academic policies

## 6. Data Requirements

The project will require:

- University knowledge documents
- Labelled student questions
- Training data
- Validation/test data

## 7. Frontend Requirements

The system should provide a simple web interface through which
students can:

- Enter questions
- Submit questions
- View answers
- View sources

## 8. Backend Requirements

The backend should:

- Receive student questions
- Process the question
- Invoke the ML classifier
- Retrieve relevant information
- Generate the response
- Return the answer to the frontend

## 9. Non-Functional Requirements

The system should be:

- Easy to use
- Reliable
- Maintainable
- Reasonably responsive
- Source-grounded
- Scalable for additional documents

## 10. Testing Requirements

The system should be evaluated using:

- ML classification metrics
- Retrieval evaluation
- Answer quality evaluation
- Functional testing

## 11. Project Limitations

The chatbot will only be expected to answer questions
supported by the available knowledge base.

It should not invent university rules or information that
cannot be verified from the available sources.