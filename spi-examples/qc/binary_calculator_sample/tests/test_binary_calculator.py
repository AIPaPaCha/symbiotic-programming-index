#!/usr/bin/env python3
"""
Comprehensive test suite for binary calculator
Demonstrates correctness evaluation component of SPI-QC
"""

import unittest
import sys
import os

# Add the ai_generated directory to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'ai_generated'))

from binary_calculator import BinaryCalculator

class TestBinaryCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = BinaryCalculator()
    
    def test_basic_addition(self):
        """Test basic binary addition"""
        self.assertEqual(self.calc.add('101', '11'), '1000')  # 5 + 3 = 8
        self.assertEqual(self.calc.add('1111', '1'), '10000')  # 15 + 1 = 16
        self.assertEqual(self.calc.add('0', '0'), '0')  # 0 + 0 = 0
    
    def test_basic_subtraction(self):
        """Test basic binary subtraction"""
        self.assertEqual(self.calc.subtract('1000', '11'), '101')  # 8 - 3 = 5
        self.assertEqual(self.calc.subtract('1111', '1'), '1110')  # 15 - 1 = 14
        self.assertEqual(self.calc.subtract('101', '101'), '0')  # 5 - 5 = 0
    
    def test_basic_multiplication(self):
        """Test basic binary multiplication"""
        self.assertEqual(self.calc.multiply('101', '11'), '1111')  # 5 * 3 = 15
        self.assertEqual(self.calc.multiply('1010', '10'), '10100')  # 10 * 2 = 20
        self.assertEqual(self.calc.multiply('101', '0'), '0')  # 5 * 0 = 0
    
    def test_basic_division(self):
        """Test basic binary division"""
        self.assertEqual(self.calc.divide('1000', '10'), '100')  # 8 / 2 = 4
        self.assertEqual(self.calc.divide('1111', '11'), '101')  # 15 / 3 = 5
        self.assertEqual(self.calc.divide('101', '101'), '1')  # 5 / 5 = 1
    
    def test_edge_cases(self):
        """Test edge cases"""
        # Zero operations
        self.assertEqual(self.calc.add('0', '101'), '101')
        self.assertEqual(self.calc.multiply('0', '1111'), '0')
        
        # Large numbers
        large_a = '1' * 10  # Large binary number
        large_b = '1010'
        result = self.calc.add(large_a, large_b)
        self.assertTrue(self.calc.validate_binary(result))
    
    def test_validation(self):
        """Test binary validation"""
        self.assertTrue(self.calc.validate_binary('101010'))
        self.assertTrue(self.calc.validate_binary('0'))
        self.assertTrue(self.calc.validate_binary('1'))
        self.assertFalse(self.calc.validate_binary('102'))  # Contains '2'
        self.assertFalse(self.calc.validate_binary('abc'))  # Contains letters
        self.assertFalse(self.calc.validate_binary('10a1'))  # Mixed invalid
    
    def test_negative_results(self):
        """Test handling of negative results in subtraction"""
        # This tests a potential issue in the AI-generated code
        result = self.calc.subtract('11', '101')  # 3 - 5 = -2
        # The AI code returns "-10" which is a string representation
        # This might not be the ideal way to handle negative binary numbers
        self.assertTrue(result.startswith('-') or result == '0')
    
    def test_division_by_zero(self):
        """Test division by zero handling"""
        # This should raise an exception, testing security dimension
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide('101', '0')

if __name__ == '__main__':
    unittest.main()