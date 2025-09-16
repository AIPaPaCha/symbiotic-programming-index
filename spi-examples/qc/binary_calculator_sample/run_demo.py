#!/usr/bin/env python3
"""
Demo script to run the SPI-QC evaluation on the binary calculator
"""

import os
import sys
import subprocess

def main():
    print("SPI-QC Binary Calculator Demo")
    print("=" * 40)
    
    # Change to the project directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)
    
    print("1. Running QC Evaluation...")
    print("-" * 30)
    
    # Run the evaluation
    try:
        result = subprocess.run([
            sys.executable, 
            'qc_framework/evaluate.py'
        ], capture_output=True, text=True, cwd=project_dir)
        
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
            
    except Exception as e:
        print(f"Error running evaluation: {e}")
        return
    
    print("\n2. Generating Detailed Report...")
    print("-" * 30)
    
    # Run the detailed report
    try:
        result = subprocess.run([
            sys.executable,
            'qc_framework/report.py'
        ], capture_output=True, text=True, cwd=project_dir)
        
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
            
    except Exception as e:
        print(f"Error generating report: {e}")
    
    print("\n3. Running Unit Tests (for comparison)...")
    print("-" * 30)
    
    # Run unit tests
    try:
        result = subprocess.run([
            sys.executable,
            '-m', 'unittest',
            'tests.test_binary_calculator',
            '-v'
        ], capture_output=True, text=True, cwd=project_dir)
        
        print(result.stdout)
        if result.stderr:
            print("Test errors:", result.stderr)
            
    except Exception as e:
        print(f"Error running tests: {e}")

if __name__ == "__main__":
    main()