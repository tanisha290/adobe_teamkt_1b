import argparse
import json
import os
from datetime import datetime
from pdf_processing import extract_sections
from section_ranking import rank_sections
from subsection_analysis import analyze_subsections

def parse_args():
    parser = argparse.ArgumentParser(description="Persona-Driven Document Intelligence System")
    parser.add_argument('--input', required=False, help='Path to input JSON file with documents, persona, and job')
    parser.add_argument('--documents', nargs='+', required=False, help='List of input PDF file paths')
    parser.add_argument('--persona', required=False, help='Path to persona definition JSON')
    parser.add_argument('--job', required=False, help='Path to job-to-be-done JSON')
    parser.add_argument('--output', required=True, help='Path to output JSON file')
    return parser.parse_args()

def get_filename(path):
    return os.path.basename(path)

def main():
    args = parse_args()
    if args.input:
        with open(args.input, 'r', encoding='utf-8') as f:
            input_data = json.load(f)
        
        # Determine the PDF folder path based on the input JSON location
        input_dir = os.path.dirname(args.input)
        pdf_folder = os.path.join(input_dir, 'PDFs')
        
        # Build document paths using the PDF folder
        documents = [os.path.join(pdf_folder, doc['filename']) for doc in input_data['documents']]
        persona = input_data['persona']
        job = input_data['job_to_be_done']
        persona_str = persona["role"] if isinstance(persona, dict) else str(persona)
        job_str = job["task"] if isinstance(job, dict) else str(job)
    else:
        from persona_job import load_persona_job
        documents = args.documents
        persona = load_persona_job(args.persona)
        job = load_persona_job(args.job)
        persona_str = persona["role"] if isinstance(persona, dict) else str(persona)
        job_str = job["task"] if isinstance(job, dict) else str(job)
    # Extract sections from PDFs
    sections = extract_sections(documents)
    # Rank sections by relevance
    ranked_sections = rank_sections(sections, persona, job)
    # Analyze sub-sections from top-ranked sections
    subsection_analysis = analyze_subsections(ranked_sections, persona, job, top_n=5)
    # Format output
    output = {
        "metadata": {
            "input_documents": [get_filename(doc) for doc in documents],
            "persona": persona_str,
            "job_to_be_done": job_str,
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": [
            {
                "document": get_filename(sec["document"]),
                "section_title": sec["section_title"],
                "importance_rank": sec["importance_rank"],
                "page_number": sec["page_number"]
            } for sec in ranked_sections[:10]
        ],
        "subsection_analysis": [
            {
                "document": get_filename(sub["document"]),
                "refined_text": sub["refined_text"],
                "page_number": sub["page_number"]
            } for sub in subsection_analysis
        ]
    }
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=4)
    print(f"Output written to {args.output}")

if __name__ == "__main__":
    main() 