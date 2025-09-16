#!/usr/bin/env python3
"""
SPI-QC Framework Implementation
Evaluates code across four dimensions: Correctness, Efficiency, Security, Conformance
"""

import time
import subprocess
import sys
import os
import tracemalloc
from typing import Dict, List, Tuple, Any
import ast
import re

class QCEvaluator:
    def __init__(self, target_file: str):
        self.target_file = target_file
        self.results = {
            'correctness': 0.0,
            'efficiency': 0.0,
            'security': 0.0,
            'conformance': 0.0,
            'overall': 0.0
        }
        self.details = {}
        
    def evaluate_correctness(self) -> float:
        """Evaluate correctness using functional tests"""
        print("Evaluating Correctness...")
        
        # Import the module for testing
        sys.path.insert(0, os.path.dirname(self.target_file))
        module_name = os.path.basename(self.target_file).replace('.py', '')
        
        try:
            module = __import__(module_name)
            calc = module.BinaryCalculator()
            
            test_cases = [
                # (operation, a, b, expected)
                ('add', '101', '11', '1000'),  # 5 + 3 = 8
                ('add', '1111', '1', '10000'),  # 15 + 1 = 16
                ('subtract', '1000', '11', '101'),  # 8 - 3 = 5
                ('multiply', '101', '11', '1111'),  # 5 * 3 = 15
                ('divide', '1000', '10', '100'),  # 8 / 2 = 4
                ('add', '0', '0', '0'),  # Edge case: zeros
                ('multiply', '101', '0', '0'),  # Edge case: multiply by zero
            ]
            
            passed = 0
            total = len(test_cases)
            failed_tests = []
            
            for op, a, b, expected in test_cases:
                try:
                    if op == 'add':
                        result = calc.add(a, b)
                    elif op == 'subtract':
                        result = calc.subtract(a, b)
                    elif op == 'multiply':
                        result = calc.multiply(a, b)
                    elif op == 'divide':
                        result = calc.divide(a, b)
                    
                    if result == expected:
                        passed += 1
                    else:
                        failed_tests.append(f"{op}({a}, {b}): got {result}, expected {expected}")
                        
                except Exception as e:
                    failed_tests.append(f"{op}({a}, {b}): Exception - {str(e)}")
            
            score = passed / total
            self.details['correctness'] = {
                'passed': passed,
                'total': total,
                'failed_tests': failed_tests,
                'score': score
            }
            
            return score
            
        except Exception as e:
            self.details['correctness'] = {'error': str(e), 'score': 0.0}
            return 0.0
    
    def evaluate_efficiency(self) -> float:
        """Evaluate efficiency through runtime and memory profiling"""
        print("Evaluating Efficiency...")
        
        try:
            sys.path.insert(0, os.path.dirname(self.target_file))
            module_name = os.path.basename(self.target_file).replace('.py', '')
            module = __import__(module_name)
            calc = module.BinaryCalculator()
            
            # Test operations with larger numbers
            test_operations = [
                ('add', '1' * 20, '1' * 15),
                ('multiply', '1111', '1010'),
                ('subtract', '1' * 25, '101010'),
            ]
            
            total_time = 0
            max_memory = 0
            
            for op, a, b in test_operations:
                tracemalloc.start()
                start_time = time.perf_counter()
                
                try:
                    if op == 'add':
                        calc.add(a, b)
                    elif op == 'multiply':
                        calc.multiply(a, b)
                    elif op == 'subtract':
                        calc.subtract(a, b)
                except:
                    pass
                
                end_time = time.perf_counter()
                current, peak = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                
                total_time += (end_time - start_time)
                max_memory = max(max_memory, peak)
            
            # Simple scoring: faster is better, less memory is better
            # Normalize against reasonable thresholds
            time_score = max(0, 1 - (total_time / 0.001))  # 1ms threshold
            memory_score = max(0, 1 - (max_memory / (1024 * 1024)))  # 1MB threshold
            
            efficiency_score = (time_score + memory_score) / 2
            
            self.details['efficiency'] = {
                'total_time': total_time,
                'max_memory': max_memory,
                'time_score': time_score,
                'memory_score': memory_score,
                'score': efficiency_score
            }
            
            return efficiency_score
            
        except Exception as e:
            self.details['efficiency'] = {'error': str(e), 'score': 0.5}
            return 0.5
    
    def evaluate_security(self) -> float:
        """Evaluate security through static analysis"""
        print("Evaluating Security...")
        
        try:
            with open(self.target_file, 'r') as f:
                code = f.read()
            
            security_issues = []
            
            # Check for common security issues
            if 'eval(' in code or 'exec(' in code:
                security_issues.append("Use of eval/exec - code injection risk")
            
            if 'input(' in code and 'int(' in code:
                security_issues.append("Potential integer overflow from user input")
            
            # Check for division without zero check
            if '/' in code or '//' in code:
                if 'ZeroDivisionError' not in code and 'if' not in code.split('//')[0]:
                    security_issues.append("Division without zero check")
            
            # Check for exception handling
            if 'except:' in code:
                security_issues.append("Bare except clause - may hide security issues")
            
            # Simple scoring based on issues found
            base_score = 1.0
            penalty_per_issue = 0.2
            security_score = max(0, base_score - (len(security_issues) * penalty_per_issue))
            
            self.details['security'] = {
                'issues': security_issues,
                'issue_count': len(security_issues),
                'score': security_score
            }
            
            return security_score
            
        except Exception as e:
            self.details['security'] = {'error': str(e), 'score': 0.5}
            return 0.5
    
    def evaluate_conformance(self) -> float:
        """Evaluate conformance to coding standards"""
        print("Evaluating Conformance...")
        
        try:
            with open(self.target_file, 'r') as f:
                code = f.read()
            
            conformance_issues = []
            
            # Check for docstrings
            tree = ast.parse(code)
            classes_with_docstrings = 0
            functions_with_docstrings = 0
            total_classes = 0
            total_functions = 0
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    total_classes += 1
                    if ast.get_docstring(node):
                        classes_with_docstrings += 1
                elif isinstance(node, ast.FunctionDef):
                    total_functions += 1
                    if ast.get_docstring(node):
                        functions_with_docstrings += 1
            
            # Check line length (PEP 8: max 79 characters)
            long_lines = 0
            lines = code.split('\n')
            for i, line in enumerate(lines):
                if len(line) > 79:
                    long_lines += 1
            
            # Check for proper naming conventions
            naming_issues = 0
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if not re.match(r'^[a-z_][a-z0-9_]*$', node.name):
                        naming_issues += 1
                elif isinstance(node, ast.ClassDef):
                    if not re.match(r'^[A-Z][a-zA-Z0-9]*$', node.name):
                        naming_issues += 1
            
            # Calculate scores
            doc_score = 0
            if total_classes > 0 or total_functions > 0:
                doc_coverage = (classes_with_docstrings + functions_with_docstrings) / (total_classes + total_functions)
                doc_score = doc_coverage
            
            line_length_score = max(0, 1 - (long_lines / len(lines)))
            naming_score = max(0, 1 - (naming_issues / max(1, total_classes + total_functions)))
            
            conformance_score = (doc_score + line_length_score + naming_score) / 3
            
            self.details['conformance'] = {
                'documentation_coverage': doc_score,
                'line_length_score': line_length_score,
                'naming_score': naming_score,
                'long_lines': long_lines,
                'naming_issues': naming_issues,
                'score': conformance_score
            }
            
            return conformance_score
            
        except Exception as e:
            self.details['conformance'] = {'error': str(e), 'score': 0.5}
            return 0.5
    
    def calculate_overall_score(self, weights: Dict[str, float] = None) -> float:
        """Calculate overall QC score using weighted harmonic mean"""
        if weights is None:
            weights = {'correctness': 0.25, 'efficiency': 0.25, 'security': 0.25, 'conformance': 0.25}
        
        epsilon = 1e-6
        harmonic_sum = 0
        
        for dimension, weight in weights.items():
            score = self.results[dimension]
            harmonic_sum += weight / (score + epsilon)
        
        overall_score = 1 / harmonic_sum
        return overall_score
    
    def run_evaluation(self) -> Dict[str, Any]:
        """Run complete QC evaluation"""
        print(f"Starting QC evaluation for: {self.target_file}")
        print("=" * 50)
        
        self.results['correctness'] = self.evaluate_correctness()
        self.results['efficiency'] = self.evaluate_efficiency()
        self.results['security'] = self.evaluate_security()
        self.results['conformance'] = self.evaluate_conformance()
        self.results['overall'] = self.calculate_overall_score()
        
        return {
            'scores': self.results,
            'details': self.details
        }