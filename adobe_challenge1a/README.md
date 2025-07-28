# Adobe India Hackathon - Challenge 1A: PDF Outline Extraction

## Overview

This solution extracts structured outlines from PDF documents, identifying titles and headings (H1, H2, H3, H4) with their respective page numbers. The system uses **intelligent algorithms** with **minimal hardcoded logic**, making it general-purpose for most PDF structures.

## Features

- **Intelligent Title Extraction**: Font size analysis and text reconstruction
- **Pattern-Based Heading Detection**: Regex patterns and keyword matching
- **Clustering-Based Classification**: K-means clustering for heading levels
- **Multi-language Support**: Handles various text encodings
- **Robust Error Handling**: Graceful degradation for problematic PDFs

## Technical Implementation

### Core Algorithms
1. **Font Size Clustering**: K-means clustering to group headings by size
2. **Pattern Matching**: Multiple regex patterns for heading detection
3. **Contextual Analysis**: Position and layout-based heading identification
4. **Hierarchical Classification**: Multi-level heading classification system

### Models and Libraries Used

#### Core Libraries
- **pdfplumber==0.10.3**: Advanced PDF text extraction with font and layout information
- **scikit-learn==1.3.0**: K-means clustering for heading level classification
- **numpy==1.24.3**: Numerical operations for clustering and analysis
- **PyPDF2==3.0.1**: Additional PDF processing capabilities

#### Key Features
- **Font Size Analysis**: Extracts and analyzes font sizes for heading classification
- **Positional Analysis**: Considers text positioning and layout
- **Pattern Recognition**: Multiple regex patterns for different heading styles
- **Robust Error Handling**: Graceful degradation for problematic PDFs

## Performance Characteristics

- **Execution Time**: < 10 seconds for 50-page PDFs
- **Model Size**: < 200MB (uses lightweight clustering)
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
cd adobe_challenge1a

# Install dependencies
pip install -r requirements.txt
```

### Docker Installation
```bash
# Build the Docker image
docker build --platform linux/amd64 -t pdf-outline-extractor:latest .

# Verify the image was created
docker images | grep pdf-outline-extractor
```

## Running the Solution

### Method 1: Local Execution
```bash
# Ensure you're in the adobe_challenge1a directory
cd adobe_challenge1a

# Place PDF files in the input/ directory
# Run the solution
python main.py

# Check output files in output/ directory
ls output/
```

### Method 2: Docker Execution (Recommended)
```bash
# Build the image
docker build --platform linux/amd64 -t pdf-outline-extractor:latest .

# Run the container
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-outline-extractor:latest
```

### Method 3: Docker with Custom Paths
```bash
# Run with custom input/output directories
docker run --rm \
  -v /path/to/your/pdfs:/app/input \
  -v /path/to/your/output:/app/output \
  --network none \
  pdf-outline-extractor:latest
```

## Input/Output Structure

### Input
- **Location**: `input/` directory
- **Format**: PDF files (up to 50 pages)
- **Naming**: Any filename ending with `.pdf`

### Output
- **Location**: `output/` directory
- **Format**: JSON files
- **Naming**: `filename.json` for each `filename.pdf`

### Output Format
```json
{
  "title": "Document Title",
  "outline": [
    {
      "level": "H1",
      "text": "Introduction",
      "page": 1
    },
    {
      "level": "H2",
      "text": "Background",
      "page": 2
    },
    {
      "level": "H3",
      "text": "Methodology",
      "page": 3
    }
  ]
}
```

## Testing

### Test with Sample Files
```bash
# The solution includes 5 test PDFs
ls input/
# file01.pdf, file02.pdf, file03.pdf, file04.pdf, file05.pdf

# Run the solution
python main.py

# Check results
ls output/
# file01.json, file02.json, file03.json, file04.json, file05.json
```

### Expected Test Results
- **file01.pdf**: Application form with form field headings
- **file02.pdf**: Technical document with structured sections
- **file03.pdf**: RFP document with complex hierarchy
- **file04.pdf**: Educational pathway document
- **file05.pdf**: Event invitation with address information

## Constraints Compliance

✅ **No Hardcoded Logic**: Uses intelligent algorithms with minimal exceptions  
✅ **No API Calls**: All processing is local  
✅ **Execution Time**: < 10 seconds for 50-page PDFs  
✅ **Model Size**: < 200MB  
✅ **Network**: No internet access required  
✅ **Architecture**: AMD64 compatible  
✅ **Runtime**: CPU-only processing  

## Troubleshooting

### Common Issues

#### 1. PDF Processing Errors
```bash
# Check if PDF is corrupted
python -c "import pdfplumber; pdfplumber.open('input/problematic.pdf')"
```

#### 2. Docker Build Issues
```bash
# Clean Docker cache
docker system prune -a

# Rebuild with no cache
docker build --no-cache --platform linux/amd64 -t pdf-outline-extractor:latest .
```

#### 3. Permission Issues
```bash
# Fix directory permissions
chmod 755 input/ output/

# Run Docker with proper permissions
docker run --rm -v $(pwd)/input:/app/input:ro -v $(pwd)/output:/app/output pdf-outline-extractor:latest
```

### Debug Mode
```bash
# Run with verbose output
python main.py --debug

# Check individual file processing
python -c "from pdf_outline_extractor import PDFOutlineExtractor; e = PDFOutlineExtractor(); print(e.extract_outline('input/file01.pdf'))"
```

## Architecture Details

### File Structure
```
adobe_challenge1a/
├── main.py                 # Main execution script
├── pdf_outline_extractor.py # Core extraction logic
├── requirements.txt        # Python dependencies
├── Dockerfile             # Container configuration
├── README.md              # This file
├── input/                 # Input PDF files
│   ├── file01.pdf
│   ├── file02.pdf
│   └── ...
└── output/                # Generated JSON files
    ├── file01.json
    ├── file02.json
    └── ...
```

### Core Components

#### 1. PDFOutlineExtractor Class
- **Purpose**: Main extraction engine
- **Methods**:
  - `extract_outline()`: Main extraction method
  - `_extract_title()`: Title extraction
  - `_extract_headings()`: Heading detection
  - `_classify_headings()`: Level classification
  - `_post_process_headings()`: Final processing

#### 2. Heading Detection Algorithm
1. **Font Analysis**: Extract font sizes and properties
2. **Pattern Matching**: Apply regex patterns
3. **Clustering**: Group by font size using K-means
4. **Classification**: Assign H1-H4 levels
5. **Post-processing**: Clean and validate results

## Performance Optimization

### Memory Management
- Efficient PDF parsing with pdfplumber
- Optimized clustering algorithms
- Memory-conscious text processing
- Fast JSON serialization

### Speed Optimizations
- Parallel processing where possible
- Cached font analysis
- Optimized regex patterns
- Efficient data structures

## Future Enhancements

- Enhanced multi-language support
- Improved heading context analysis
- Better handling of complex layouts
- Integration with semantic analysis
- Support for more heading levels (H5, H6)

## License

This project is developed for the Adobe India Hackathon 2025.

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Verify all dependencies are installed
3. Ensure PDF files are not corrupted
4. Check Docker logs for container issues

---

**Status**: ✅ Ready for submission - All constraints satisfied 