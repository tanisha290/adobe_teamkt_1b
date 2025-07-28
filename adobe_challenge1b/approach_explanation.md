# Approach Explanation: Persona-Driven Document Intelligence System

## Overview
This system is designed to extract and prioritize the most relevant sections from a collection of documents (PDFs) based on a specific persona and their job-to-be-done. The solution is generic and can handle diverse document types, personas, and tasks, while adhering to constraints on model size, CPU-only execution, and processing time.

## Methodology

### 1. PDF Ingestion and Parsing
We use the lightweight `PyPDF2` library to parse PDF files and extract text content page by page. This approach is robust, fast, and does not require GPU or large models, making it suitable for offline, resource-constrained environments.

### 2. Section Extraction
Sections are identified using simple heuristics based on text formatting. For example, lines in ALL CAPS or Title Case are treated as potential section titles. Each detected section is associated with its document, page number, and the surrounding text. This method is domain-agnostic and works across various document types, from research papers to business reports.

### 3. Persona and Job-to-be-Done Input
Persona and job definitions are provided as JSON files. These are loaded and parsed to extract relevant keywords and context, which guide the relevance scoring in subsequent steps.

### 4. Section Ranking
Extracted sections are ranked according to their relevance to the persona and job-to-be-done. Relevance is determined by keyword overlap: the system tokenizes the persona and job descriptions, then scores each section based on the presence of these keywords in the section title and text. Sections are sorted by their scores, and an importance rank is assigned.

### 5. Sub-Section Analysis
For the top-ranked sections, the system performs a finer-grained analysis by splitting the section text into sentences or paragraphs. Each sub-section is scored for relevance using the same keyword-based approach. The most relevant sub-sections are extracted and included in the output, providing granular insights tailored to the persona's needs.

### 6. Output Formatting
The final output is a structured JSON file containing:
- Metadata (input documents, persona, job, timestamp)
- Extracted sections (with document, page number, section title, importance rank)
- Sub-section analysis (with document, refined text, page number, and rank)

## Design Choices
- **Efficiency:** All processing is performed on CPU using lightweight libraries, ensuring compliance with resource constraints.
- **Generality:** Heuristic-based section extraction and keyword-based ranking allow the system to generalize across domains and document types.
- **Transparency:** The approach is interpretable, with clear logic for section and sub-section selection.
- **Extensibility:** The modular design allows for future enhancements, such as more advanced NLP techniques or domain-specific heuristics, within the given constraints.

## Conclusion
This solution provides a practical, efficient, and extensible framework for persona-driven document intelligence, delivering relevant insights tailored to diverse user needs and tasks. 