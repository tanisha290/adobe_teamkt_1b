from typing import List, Dict
import re
import json

def analyze_subsections(ranked_sections: List[Dict], persona: Dict, job: Dict, top_n: int = 5) -> List[Dict]:
    """
    For top-N ranked sections, extract and rank sentences/paragraphs by relevance.
    Returns a list of dicts with document, refined_text, and page_number.
    """
    persona_keywords = set(re.findall(r'\w+', json.dumps(persona).lower()))
    job_keywords = set(re.findall(r'\w+', json.dumps(job).lower()))
    all_keywords = persona_keywords | job_keywords
    results = []
    for section in ranked_sections[:top_n]:
        text = section.get('text', '')
        sentences = re.split(r'(?<=[.!?])\s+', text)
        scored = []
        for sent in sentences:
            score = sum(1 for kw in all_keywords if kw in sent.lower())
            if score > 0:
                scored.append((score, sent))
        scored.sort(reverse=True)
        for rank, (score, sent) in enumerate(scored[:3]):  # Top 3 per section
            results.append({
                'document': section['document'],
                'refined_text': sent.strip(),
                'page_number': section['page_number'],
                'subsection_rank': rank + 1
            })
    return results 