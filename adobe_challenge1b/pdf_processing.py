import PyPDF2
from typing import List, Dict
import re

TRAVEL_KEYWORDS = [
    'guide', 'adventure', 'experience', 'tips', 'tricks', 'packing', 'nightlife', 'entertainment',
    'coastal', 'culinary', 'water sports', 'itinerary', 'things to do', 'restaurants', 'hotels', 'culture', 'history', 'cities'
]

def extract_sections(pdf_paths: List[str]) -> List[Dict]:
    """
    For each page, extract the first non-empty line as a section title, and also scan for lines with travel-relevant keywords.
    Store the full page text for sub-section analysis.
    """
    results = []
    for pdf_path in pdf_paths:
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for i, page in enumerate(reader.pages):
                text = page.extract_text() or ""
                lines = [line.strip() for line in text.split('\n') if line.strip()]
                # Find candidate section titles
                section_title = None
                for line in lines:
                    if any(kw in line.lower() for kw in TRAVEL_KEYWORDS):
                        section_title = line
                        break
                if not section_title and lines:
                    section_title = lines[0]  # fallback: first non-empty line
                if section_title:
                    results.append({
                        'document': pdf_path,
                        'page_number': i + 1,
                        'section_title': section_title,
                        'text': text.strip()
                    })
    return results 