# Adobe India Hackathon - Challenge 1B: Persona-Driven Document Intelligence

## Overview

This solution intelligently analyzes document collections based on specific persona requirements and job-to-be-done scenarios. The system extracts and prioritizes the most relevant sections from multiple documents, providing contextually relevant insights for different user types and tasks.

## Features

- **Dynamic Persona Analysis**: Extracts keywords from persona descriptions automatically
- **Intelligent Content Ranking**: Multi-dimensional scoring algorithm for relevance
- **Cross-Document Analysis**: Identifies patterns across document collections
- **Subsection Extraction**: Granular content analysis with relevance scoring
- **Generic Architecture**: Works with any domain, persona, or task type

## Technical Implementation

### Core Algorithms
1. **TF-IDF Vectorization**: Converts document sections into vector representations
2. **Cosine Similarity**: Calculates semantic relevance between content and requirements
3. **Multi-Dimensional Scoring**: Combines semantic similarity with keyword matching
4. **Content Segmentation**: Paragraph-level analysis and extraction

### Models and Libraries Used

#### Core Libraries
- **PyPDF2==3.0.1**: PDF text extraction and processing
- **scikit-learn**: TF-IDF vectorization and cosine similarity (if needed)
- **numpy**: Numerical operations for scoring and ranking
- **re**: Regular expressions for text processing

#### Key Features
- **Persona Adaptation**: Dynamic keyword extraction and scoring
- **Cross-Document Analysis**: Identifies relevant content across multiple documents
- **Contextual Intelligence**: Maintains document structure and relationships
- **Robust Error Handling**: Graceful degradation for problematic documents

## Performance Characteristics

- **Execution Time**: < 60 seconds for 3-5 documents
- **Model Size**: < 1GB (lightweight approach)
- **Memory Usage**: Optimized for 16GB RAM systems
- **CPU Usage**: Efficient multi-core processing

## Installation

### Prerequisites
- Python 3.8+
- Docker (for containerized execution)

### Local Installation
```bash
# Clone the repository
git clone <repository-url>
cd adobe_challenge1b

# Install dependencies
pip install -r requirements.txt
```

### Docker Installation
```bash
# Build the Docker image
docker build --platform linux/amd64 -t persona-document-analyzer:latest .

# Verify the image was created
docker images | grep persona-document-analyzer
```

## Running the Solution

### Method 1: Local Execution (Single Collection)
```bash
# Ensure you're in the adobe_challenge1b directory
cd adobe_challenge1b

# Run with input JSON file
python main.py --input input/Collection\ 1/challenge1b_input.json --output output/collection1_result.json

# Or run with individual parameters
python main.py --documents input/Collection\ 1/PDFs/*.pdf --persona "Travel Planner" --job "Plan a trip" --output output/result.json
```

### Method 2: Docker Execution (Recommended)
```bash
# Build the image
docker build --platform linux/amd64 -t persona-document-analyzer:latest .

# Run the container
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  persona-document-analyzer:latest \
  --input input/Collection\ 1/challenge1b_input.json \
  --output output/collection1_result.json
```

### Method 3: Process All Collections
```bash
# Run all three test collections
python run_all_collections.py
```

### Method 4: Docker with Custom Paths
```bash
# Run with custom input/output directories
docker run --rm \
  -v /path/to/your/input:/app/input \
  -v /path/to/your/output:/app/output \
  --network none \
  persona-document-analyzer:latest \
  --input input/your_collection/challenge1b_input.json \
  --output output/your_result.json
```

## Input/Output Structure

### Input Configuration
Create a JSON file with the following structure:
```json
{
  "documents": [
    {"filename": "document1.pdf"},
    {"filename": "document2.pdf"},
    {"filename": "document3.pdf"}
  ],
  "persona": {
    "role": "PhD Researcher in Computational Biology",
    "expertise": ["machine learning", "bioinformatics", "data analysis"]
  },
  "job_to_be_done": {
    "task": "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks",
    "requirements": ["methodology", "datasets", "benchmarks"]
  }
}
```

### Input Directory Structure
```
input/
├── Collection 1/
│   ├── challenge1b_input.json
│   └── PDFs/
│       ├── South of France - Cities.pdf
│       ├── South of France - Cuisine.pdf
│       └── ...
├── Collection 2/
│   ├── challenge1b_input.json
│   └── PDFs/
│       ├── Learn Acrobat - Create and Convert_1.pdf
│       └── ...
└── Collection 3/
    ├── challenge1b_input.json
    └── PDFs/
        ├── Breakfast Ideas.pdf
        └── ...
```

### Output Format
```json
{
  "metadata": {
    "input_documents": ["document1.pdf", "document2.pdf"],
    "persona": "PhD Researcher in Computational Biology",
    "job_to_be_done": "Prepare a comprehensive literature review...",
    "processing_timestamp": "2024-01-01T12:00:00"
  },
  "extracted_sections": [
    {
      "document": "research_paper_1.pdf",
      "section_title": "Methodology",
      "importance_rank": 1,
      "page_number": 3
    }
  ],
  "subsection_analysis": [
    {
      "document": "research_paper_1.pdf",
      "refined_text": "The experimental setup consisted of...",
      "page_number": 3
    }
  ]
}
```

## Testing

### Test with Sample Collections
```bash
# The solution includes 3 test collections
ls input/
# Collection 1/, Collection 2/, Collection 3/

# Run all collections
python run_all_collections.py

# Check results
ls output/
# collection1_result.json, collection2_result.json, collection3_result.json
```

### Expected Test Results
- **Collection 1**: Travel Planner persona with South of France documents
- **Collection 2**: HR Professional persona with Acrobat learning documents
- **Collection 3**: Food Contractor persona with recipe documents

## Constraints Compliance

✅ **Execution Time**: < 60 seconds for document collections  
✅ **Model Size**: < 1GB  
✅ **Network**: No internet access required  
✅ **Architecture**: AMD64 compatible  
✅ **Runtime**: CPU-only processing  
✅ **Generic Solution**: Works with any domain and persona  

## Troubleshooting

### Common Issues

#### 1. PDF Processing Errors
```bash
# Check if PDF is corrupted
python -c "import PyPDF2; PyPDF2.PdfReader('input/Collection\ 1/PDFs/document.pdf')"
```

#### 2. Docker Build Issues
```bash
# Clean Docker cache
docker system prune -a

# Rebuild with no cache
docker build --no-cache --platform linux/amd64 -t persona-document-analyzer:latest .
```

#### 3. Permission Issues
```bash
# Fix directory permissions
chmod 755 input/ output/

# Run Docker with proper permissions
docker run --rm -v $(pwd)/input:/app/input:ro -v $(pwd)/output:/app/output persona-document-analyzer:latest
```

#### 4. Collection Processing Issues
```bash
# Check input JSON format
python -c "import json; print(json.load(open('input/Collection\ 1/challenge1b_input.json')))"

# Verify PDF files exist
ls input/Collection\ 1/PDFs/
```

### Debug Mode
```bash
# Run with verbose output
python main.py --input input/Collection\ 1/challenge1b_input.json --output output/debug.json --debug

# Check individual component
python -c "from pdf_processing import extract_sections; print(extract_sections(['input/Collection\ 1/PDFs/document.pdf']))"
```

## Architecture Details

### File Structure
```
adobe_challenge1b/
├── main.py                 # Main execution script
├── pdf_processing.py       # PDF text extraction
├── section_ranking.py      # Relevance scoring
├── subsection_analysis.py  # Granular content analysis
├── run_all_collections.py  # Batch processing script
├── requirements.txt        # Python dependencies
├── Dockerfile             # Container configuration
├── README.md              # This file
├── approach_explanation.md # Methodology explanation
├── input/                 # Input collections
│   ├── Collection 1/
│   ├── Collection 2/
│   └── Collection 3/
└── output/                # Generated results
    ├── collection1_result.json
    ├── collection2_result.json
    └── collection3_result.json
```

### Core Components

#### 1. PDF Processing Module
- **Purpose**: Extract text and sections from PDFs
- **Methods**:
  - `extract_sections()`: Main extraction method
  - Keyword-based section identification
  - Page-level text extraction

#### 2. Section Ranking Module
- **Purpose**: Score sections by relevance to persona/job
- **Methods**:
  - `rank_sections()`: Main ranking method
  - Keyword overlap scoring
  - Multi-dimensional relevance calculation

#### 3. Subsection Analysis Module
- **Purpose**: Extract granular content from top sections
- **Methods**:
  - `analyze_subsections()`: Main analysis method
  - Sentence-level relevance scoring
  - Content refinement and filtering

## Performance Optimization

### Memory Management
- Efficient PDF parsing with PyPDF2
- Optimized text processing
- Memory-conscious scoring algorithms
- Fast JSON serialization

### Speed Optimizations
- Parallel processing where possible
- Cached keyword extraction
- Optimized similarity calculations
- Efficient data structures

## Innovation Highlights

1. **Adaptive Persona Understanding**: Dynamic keyword extraction from persona descriptions
2. **Intelligent Content Prioritization**: Multi-dimensional scoring algorithm
3. **Cross-Document Analysis**: Identifies patterns across document collections
4. **Contextual Intelligence**: Maintains document structure and relationships

## Future Enhancements

- Advanced transformer-based semantic understanding
- Named entity recognition for better context
- Learning-based persona adaptation
- Real-time relevance updates
- Enhanced multi-language support

## License

This project is developed for the Adobe India Hackathon 2025.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all dependencies are installed
3. Ensure PDF files are not corrupted
4. Check Docker logs for container issues
5. Verify input JSON format is correct

---

**Status**: ✅ Ready for submission - All constraints satisfied 
