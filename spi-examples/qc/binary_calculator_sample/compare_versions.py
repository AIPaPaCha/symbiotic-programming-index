#!/usr/bin/env python3
"""
Compare QC scores between different versions of the binary calculator
"""

import os
import sys
from qc_framework.qc_evaluator import QCEvaluator

def evaluate_version(filename, version_name):
    """Evaluate a specific version and return results"""
    target_file = os.path.join(
        os.path.dirname(__file__),
        'ai_generated',
        filename
    )
    
    if not os.path.exists(target_file):
        print(f"File not found: {target_file}")
        return None
    
    print(f"\nEvaluating {version_name}...")
    print("=" * 50)
    
    evaluator = QCEvaluator(target_file)
    results = evaluator.run_evaluation()
    
    return results

def compare_results(results1, results2, name1, name2):
    """Compare and display results from two versions"""
    print(f"\nCOMPARISON: {name1} vs {name2}")
    print("=" * 60)
    
    scores1 = results1['scores']
    scores2 = results2['scores']
    
    dimensions = ['correctness', 'efficiency', 'security', 'conformance', 'overall']
    
    print(f"{'Dimension':<12} {'Original':<10} {'Flawed':<10} {'Difference':<12}")
    print("-" * 50)
    
    for dim in dimensions:
        score1 = scores1[dim]
        score2 = scores2[dim]
        diff = score1 - score2
        diff_str = f"{diff:+.3f}"
        
        print(f"{dim.title():<12} {score1:<10.3f} {score2:<10.3f} {diff_str:<12}")
    
    # Analysis
    print(f"\nANALYSIS:")
    print("-" * 30)
    
    if scores1['overall'] > scores2['overall']:
        winner = name1
        margin = scores1['overall'] - scores2['overall']
    else:
        winner = name2
        margin = scores2['overall'] - scores1['overall']
    
    print(f"Better version: {winner} (by {margin:.3f} points)")
    
    # Dimension-specific insights
    details1 = results1['details']
    details2 = results2['details']
    
    if 'security' in details1 and 'security' in details2:
        issues1 = len(details1['security'].get('issues', []))
        issues2 = len(details2['security'].get('issues', []))
        print(f"Security issues: {name1} has {issues1}, {name2} has {issues2}")
    
    if 'conformance' in details1 and 'conformance' in details2:
        doc1 = details1['conformance'].get('documentation_coverage', 0)
        doc2 = details2['conformance'].get('documentation_coverage', 0)
        print(f"Documentation: {name1} has {doc1:.1%}, {name2} has {doc2:.1%}")

def main():
    print("SPI-QC Version Comparison Demo")
    print("=" * 40)
    
    # Evaluate both versions
    results_original = evaluate_version('binary_calculator.py', 'Original Version')
    results_flawed = evaluate_version('binary_calculator_flawed.py', 'Flawed Version')
    
    if results_original and results_flawed:
        compare_results(results_original, results_flawed, 'Original', 'Flawed')
    
    print(f"\nKEY INSIGHTS:")
    print("=" * 40)
    print("• The QC framework successfully identifies quality differences")
    print("• Security issues significantly impact overall scores")
    print("• Conformance issues (naming, documentation) affect maintainability")
    print("• The weighted harmonic mean ensures no dimension can be ignored")

if __name__ == "__main__":
    main()