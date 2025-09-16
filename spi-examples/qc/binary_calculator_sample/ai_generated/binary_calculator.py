#!/usr/bin/env python3
"""
Binary Calculator - AI Generated Code
Simulates typical AI coder output with some quality issues for demonstration
"""

import sys

class BinaryCalculator:
    def __init__(self):
        pass
    
    def add(self, a, b):
        # Convert binary strings to integers
        num1 = int(a, 2)
        num2 = int(b, 2)
        result = num1 + num2
        return bin(result)[2:]
    
    def subtract(self, a, b):
        num1 = int(a, 2)
        num2 = int(b, 2)
        result = num1 - num2
        if result < 0:
            # Handle negative results (potential issue)
            return "-" + bin(abs(result))[2:]
        return bin(result)[2:]
    
    def multiply(self, a, b):
        num1 = int(a, 2)
        num2 = int(b, 2)
        result = num1 * num2
        return bin(result)[2:]
    
    def divide(self, a, b):
        num1 = int(a, 2)
        num2 = int(b, 2)
        # Potential security issue - no zero division check
        result = num1 // num2
        return bin(result)[2:]
    
    def validate_binary(self, binary_str):
        # Basic validation - could be more robust
        for char in binary_str:
            if char not in '01':
                return False
        return True

def main():
    calc = BinaryCalculator()
    
    print("Binary Calculator")
    print("Operations: add, subtract, multiply, divide")
    
    while True:
        try:
            operation = input("Enter operation (or 'quit'): ").strip().lower()
            
            if operation == 'quit':
                break
                
            if operation not in ['add', 'subtract', 'multiply', 'divide']:
                print("Invalid operation")
                continue
                
            a = input("Enter first binary number: ").strip()
            b = input("Enter second binary number: ").strip()
            
            if not calc.validate_binary(a) or not calc.validate_binary(b):
                print("Invalid binary input")
                continue
            
            if operation == 'add':
                result = calc.add(a, b)
            elif operation == 'subtract':
                result = calc.subtract(a, b)
            elif operation == 'multiply':
                result = calc.multiply(a, b)
            elif operation == 'divide':
                result = calc.divide(a, b)
            
            print(f"Result: {result}")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()