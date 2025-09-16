#!/usr/bin/env python3
"""
Binary Calculator - Flawed AI Generated Code
This version has intentional issues to demonstrate QC evaluation
"""

import sys

class binaryCalculator:  # Bad naming convention
    def __init__(self):
        pass
    
    def add(self, a, b):
        num1 = int(a, 2)
        num2 = int(b, 2)
        result = num1 + num2
        return bin(result)[2:]
    
    def subtract(self, a, b):
        num1 = int(a, 2)
        num2 = int(b, 2)
        result = num1 - num2
        if result < 0:
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
        result = num1 // num2  # No zero division check - security issue
        return bin(result)[2:]
    
    def validate_binary(self, binary_str):
        for char in binary_str:
            if char not in '01':
                return False
        return True
    
    def complex_operation(self, a, b, c):  # Inefficient algorithm
        # Intentionally inefficient: O(n^3) when it could be O(n)
        result = 0
        for i in range(int(a, 2)):
            for j in range(int(b, 2)):
                for k in range(int(c, 2)):
                    result += 1
        return bin(result)[2:]

def main():
    calc = binaryCalculator()
    
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
            
            # Using eval - major security issue
            if operation == 'special':
                result = eval(f"calc.{operation}('{a}', '{b}')")
            else:
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
                    result = calc.divide(a, b)  # Will crash on division by zero
            
            print(f"Result: {result}")
            
        except:  # Bare except - security issue
            print("An error occurred")

if __name__ == "__main__":
    main()