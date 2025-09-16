#!/usr/bin/env python3
"""
Detailed reporting for QC evaluation results
"""

import json
import os
import sys

def load_results():
    """Load QC evaluation results"""
    results_file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'results',
        'qc_results.json'
    )
    
    if not os.path.exists(results_file):
        print("No results found. Run evaluate.py first.")
        sys.exit(1)
    
    with open(results_file, 'r') as f:
        return json.load(f)

def print_detailed_report(results):
    """Print comprehensive QC report"""
    scores = results['scores']
    details = results['details']
    
    print("SPI-QC DETAILED EVALUATION REPORT")
    print("=" * 60)
    
    # Overall Score
    print(f"\nOVERALL QC SCORE: {scores['overall']:.3f}")
    print("(Weighted harmonic mean of all dimensions)")
    
    # Dimension Breakdown
    print("\nDIMENSION SCORES:")
    print("-" * 40)
    
    dimensions = [
        ('Correctness', 'correctness'),
        ('Efficiency', 'efficiency'), 
        ('Security', 'security'),
        ('Conformance', 'conformance')
    ]
    
    for name, key in dimensions:
        score = scores[key]
        print(f"{name:12}: {score:.3f} {'✓' if score >= 0.8 else '⚠' if score >= 0.6 else '✗'}")
    
    # Detailed Analysis
    print("\nDETAILED ANALYSIS:")
    print("=" * 60)
    
    # Correctness Details
    if 'correctness' in details:
        correctness = details['correctness']
        print(f"\n1. CORRECTNESS (Score: {scores['correctness']:.3f})")
        print("-" * 30)
        
        if 'passed' in correctness:
            print(f"Tests passed: {correctness['passed']}/{correctness['total']}")
            
            if correctness['failed_tests']:
                print("Failed tests:")
                for test in correctness['failed_tests']:
                    print(f"  ✗ {test}")
            else:
                print("  ✓ All tests passed!")
        
        if 'error' in correctness:
            print(f"Error: {correctness['error']}")
    
    # Efficiency Details
    if 'efficiency' in details:
        efficiency = details['efficiency']
        print(f"\n2. EFFICIENCY (Score: {scores['efficiency']:.3f})")
        print("-" * 30)
        
        if 'total_time' in efficiency:
            print(f"Total execution time: {efficiency['total_time']:.6f}s")
            print(f"Peak memory usage: {efficiency['max_memory']:,} bytes")
            print(f"Time performance: {efficiency['time_score']:.3f}")
            print(f"Memory performance: {efficiency['memory_score']:.3f}")
        
        if 'error' in efficiency:
            print(f"Error: {efficiency['error']}")
    
    # Security Details
    if 'security' in details:
        security = details['security']
        print(f"\n3. SECURITY (Score: {scores['security']:.3f})")
        print("-" * 30)
        
        if 'issues' in security:
            if security['issues']:
                print(f"Security issues found ({len(security['issues'])}):")
                for issue in security['issues']:
                    print(f"  ⚠ {issue}")
            else:
                print("  ✓ No security issues detected!")
        
        if 'error' in security:
            print(f"Error: {security['error']}")
    
    # Conformance Details
    if 'conformance' in details:
        conformance = details['conformance']
        print(f"\n4. CONFORMANCE (Score: {scores['conformance']:.3f})")
        print("-" * 30)
        
        if 'documentation_coverage' in conformance:
            print(f"Documentation coverage: {conformance['documentation_coverage']:.1%}")
            print(f"Line length compliance: {conformance['line_length_score']:.1%}")
            print(f"Naming convention compliance: {conformance['naming_score']:.1%}")
            
            if conformance.get('long_lines', 0) > 0:
                print(f"  ⚠ {conformance['long_lines']} lines exceed 79 characters")
            
            if conformance.get('naming_issues', 0) > 0:
                print(f"  ⚠ {conformance['naming_issues']} naming convention violations")
        
        if 'error' in conformance:
            print(f"Error: {conformance['error']}")
    
    # Recommendations
    print("\nRECOMMENDATIONS:")
    print("=" * 60)
    
    recommendations = []
    
    if scores['correctness'] < 0.8:
        recommendations.append("• Fix failing test cases to improve correctness")
    
    if scores['security'] < 0.8:
        recommendations.append("• Address security vulnerabilities (especially division by zero)")
    
    if scores['conformance'] < 0.8:
        recommendations.append("• Add docstrings to classes and methods")
        recommendations.append("• Follow PEP 8 style guidelines")
    
    if scores['efficiency'] < 0.8:
        recommendations.append("• Optimize algorithms for better performance")
    
    if not recommendations:
        recommendations.append("• Code quality is good! Consider minor optimizations.")
    
    for rec in recommendations:
        print(rec)
    
    # Quality Gate
    print(f"\nQUALITY GATE:")
    print("=" * 60)
    
    if scores['overall'] >= 0.8:
        print("✅ PASS - Code meets quality standards")
    elif scores['overall'] >= 0.6:
        print("⚠️  CONDITIONAL PASS - Code needs improvements")
    else:
        print("❌ FAIL - Code requires significant improvements")

def main():
    results = load_results()
    print_detailed_report(results)

if __name__ == "__main__":
    main()