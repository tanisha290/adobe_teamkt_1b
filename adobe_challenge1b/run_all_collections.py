#!/usr/bin/env python3
"""
Script to run challenge 1b for all three collections
"""

import os
import json
import subprocess
import sys
from pathlib import Path

def run_collection(collection_name, input_json_path, pdf_folder_path, output_path):
    """Run the challenge 1b system for a specific collection"""
    print(f"\n{'='*60}")
    print(f"Processing {collection_name}")
    print(f"{'='*60}")
    
    # Read the input JSON to get document paths
    with open(input_json_path, 'r', encoding='utf-8') as f:
        input_data = json.load(f)
    
    # Build the list of PDF file paths
    pdf_files = []
    for doc in input_data['documents']:
        pdf_path = os.path.join(pdf_folder_path, doc['filename'])
        if os.path.exists(pdf_path):
            pdf_files.append(pdf_path)
        else:
            print(f"Warning: PDF file not found: {pdf_path}")
    
    if not pdf_files:
        print(f"Error: No PDF files found for {collection_name}")
        return False
    
    # Create the command
    cmd = [
        sys.executable, 'main.py',
        '--input', input_json_path,
        '--output', output_path
    ]
    
    print(f"Running command: {' '.join(cmd)}")
    print(f"Processing {len(pdf_files)} PDF files...")
    
    try:
        # Run the command
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=os.getcwd())
        
        if result.returncode == 0:
            print(f"✅ Successfully processed {collection_name}")
            print(f"Output saved to: {output_path}")
            if result.stdout:
                print("Output:", result.stdout.strip())
        else:
            print(f"❌ Error processing {collection_name}")
            print("Error:", result.stderr.strip())
            return False
            
    except Exception as e:
        print(f"❌ Exception while processing {collection_name}: {str(e)}")
        return False
    
    return True

def main():
    """Main function to process all collections"""
    print("Starting Challenge 1b - Processing All Collections")
    print("=" * 60)
    
    # Define collections
    collections = [
        {
            "name": "Collection 1 - Travel Planner",
            "input_json": "input/Collection 1/challenge1b_input.json",
            "pdf_folder": "input/Collection 1/PDFs",
            "output": "output/collection1_result.json"
        },
        {
            "name": "Collection 2 - HR Professional", 
            "input_json": "input/Collection 2/challenge1b_input.json",
            "pdf_folder": "input/Collection 2/PDFs",
            "output": "output/collection2_result.json"
        },
        {
            "name": "Collection 3 - Food Contractor",
            "input_json": "input/Collection 3/challenge1b_input.json", 
            "pdf_folder": "input/Collection 3/PDFs",
            "output": "output/collection3_result.json"
        }
    ]
    
    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)
    
    # Process each collection
    results = []
    for collection in collections:
        success = run_collection(
            collection["name"],
            collection["input_json"],
            collection["pdf_folder"], 
            collection["output"]
        )
        results.append((collection["name"], success))
    
    # Summary
    print(f"\n{'='*60}")
    print("PROCESSING SUMMARY")
    print(f"{'='*60}")
    
    for name, success in results:
        status = "✅ SUCCESS" if success else "❌ FAILED"
        print(f"{name}: {status}")
    
    successful = sum(1 for _, success in results if success)
    total = len(results)
    print(f"\nTotal: {successful}/{total} collections processed successfully")

if __name__ == "__main__":
    main() 