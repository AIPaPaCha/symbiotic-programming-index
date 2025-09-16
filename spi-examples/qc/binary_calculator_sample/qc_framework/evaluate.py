#!/usr/bin/env python3
"""
Main evaluation script for SPI-QC Binary Calculator Sample
"""

import os
import sys
import json
from qc_evaluator import QCEvaluator

def main():
    # Path to the AI-generated binary calculator
    target_file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'ai_generated',
        'binary_calculator.py'
    )
    
    if not os.path.exists(target_file):
        print(f"Error: Target file not found: {target_file}")
        sys.exit(1)
    
    # Run QC evaluation
    evaluator = QCEvaluator(target_file)
    results = evaluator.run_evaluation()
    
    # Print results
    print("\n" + "=" * 50)
    print("QC EVALUATION RESULTS")
    print("=" * 50)
    
    scores = results['scores']
    print(f"Correctness:  {scores['correctness']:.3f}")
    print(f"Efficiency:   {scores['efficiency']:.3f}")
    print(f"Security:     {scores['security']:.3f}")
    print(f"Conformance:  {scores['conformance']:.3f}")
    print("-" * 30)
    print(f"Overall QC:   {scores['overall']:.3f}")
    
    # Save detailed results
    results_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'results')
    os.makedirs(results_dir, exist_ok=True)
    
    with open(os.path.join(results_dir, 'qc_results.json'), 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\nDetailed results saved to: {results_dir}/qc_results.json")
    
    # Print summary insights
    print("\n" + "=" * 50)
    print("INSIGHTS")
    print("=" * 50)
    
    details = results['details']
    
    if 'correctness' in details:
        correctness = details['correctness']
        if 'failed_tests' in correctness and correctness['failed_tests']:
            print("Correctness Issues:")
            for test in correctness['failed_tests']:
                print(f"  - {test}")
    
    if 'security' in details:
        security = details['security']
        if 'issues' in security and security['issues']:
            print("Security Issues:")
            for issue in security['issues']:
                print(f"  - {issue}")
    
    if 'conformance' in details:
        conformance = details['conformance']
        print(f"Code Quality:")
        print(f"  - Documentation coverage: {conformance.get('documentation_coverage', 0):.1%}")
        print(f"  - Line length compliance: {conformance.get('line_length_score', 0):.1%}")
        print(f"  - Naming convention compliance: {conformance.get('naming_score', 0):.1%}")

if __name__ == "__main__":
    main()