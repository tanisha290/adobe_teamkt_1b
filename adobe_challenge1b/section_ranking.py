from typing import List, Dict
import re
import json

def rank_sections(sections: List[Dict], persona: Dict, job: Dict) -> List[Dict]:
    """
    Assigns an importance rank to each section based on keyword overlap with persona and job.
    Returns a list of sections with 'importance_rank' field added.
    """
    # Combine keywords from persona and job
    persona_keywords = set(re.findall(r'\w+', json.dumps(persona).lower()))
    job_keywords = set(re.findall(r'\w+', json.dumps(job).lower()))
    all_keywords = persona_keywords | job_keywords

    ranked = []
    for section in sections:
        text = (section.get('section_title', '') + ' ' + section.get('text', '')).lower()
        score = sum(1 for kw in all_keywords if kw in text)
        ranked.append({**section, 'importance_rank': score})
    # Sort by descending importance
    ranked.sort(key=lambda x: x['importance_rank'], reverse=True)
    # Assign rank order
    for idx, sec in enumerate(ranked):
        sec['importance_rank'] = idx + 1
    return ranked 