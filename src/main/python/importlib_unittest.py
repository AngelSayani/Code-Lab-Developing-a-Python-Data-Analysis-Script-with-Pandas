#Unit Test for Task 1: Import Required Libraries
import unittest
import importlib.util
import sys
import os

class TestRequiredLibraries(unittest.TestCase):
    def test_required_imports(self):
        """Test that all required libraries are imported correctly"""
        # Get the path to the sales_analysis.py file
        file_path = os.path.join('src', 'main', 'python', 'sales_analysis.py')
        
        # Check if file exists
        self.assertTrue(os.path.exists(file_path), 
                        "sales_analysis.py file not found. Make sure it's in the correct location.")
        
        # Read the file content
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Check for required imports
        self.assertIn("import pandas as pd", content, 
                     "You need to import pandas with the alias 'pd'")
        
        self.assertIn("import matplotlib.pyplot as plt", content, 
                     "You need to import matplotlib.pyplot with the alias 'plt'")
        
        self.assertIn("import numpy as np", content, 
                     "You need to import numpy with the alias 'np'")

if __name__ == '__main__':
    unittest.main()
