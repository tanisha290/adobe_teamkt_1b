import os
import json
from pdf_outline_extractor import PDFOutlineExtractor

INPUT_DIR = 'input'
OUTPUT_DIR = 'output'

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def main():
    ensure_output_dir()
    extractor = PDFOutlineExtractor()
    processed = 0
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(INPUT_DIR, filename)
            output_filename = os.path.splitext(filename)[0] + '.json'
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            try:
                outline = extractor.extract_outline(pdf_path)
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(outline, f, ensure_ascii=False, indent=2)
                print(f"Processed: {filename} -> {output_filename}")
                processed += 1
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    if processed == 0:
        print("No PDF files found in input/ directory.")
    else:
        print(f"Done. {processed} PDF(s) processed.")

if __name__ == '__main__':
    main() 