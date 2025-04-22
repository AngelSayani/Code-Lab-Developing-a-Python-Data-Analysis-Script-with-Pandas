# Unit Test for Task 1: Import Required Libraries
import unittest
import importlib.util
import os
import sys

class TestRequiredLibraries(unittest.TestCase):
    def test_required_imports(self):
        """Test that all required libraries are imported correctly"""
        # Get the path to the sales_analysis.py file
        file_path = os.path.join('src', 'main', 'python', 'sales_analysis.py')
        
        print(f"\nChecking if {file_path} exists...")
        if not os.path.exists(file_path):
            print(f"ERROR: {file_path} not found!")
            self.fail(f"sales_analysis.py file not found. Make sure it's in the correct location.")
        else:
            print(f"File found at {file_path}")
        
        # Read the file content
        print("Reading file content...")
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Check for required imports
        print("\nChecking for required library imports:")
        
        # Check pandas import
        if "import pandas as pd" in content:
            print("✓ pandas is correctly imported with alias 'pd'")
        else:
            print("✗ ERROR: pandas is not imported correctly!")
            self.assertIn("import pandas as pd", content, 
                         "You need to import pandas with the alias 'pd'")
        
        # Check matplotlib import
        if "import matplotlib.pyplot as plt" in content:
            print("✓ matplotlib.pyplot is correctly imported with alias 'plt'")
        else:
            print("✗ ERROR: matplotlib.pyplot is not imported correctly!")
            self.assertIn("import matplotlib.pyplot as plt", content, 
                         "You need to import matplotlib.pyplot with the alias 'plt'")
        
        # Check numpy import
        if "import numpy as np" in content:
            print("✓ numpy is correctly imported with alias 'np'")
        else:
            print("✗ ERROR: numpy is not imported correctly!")
            self.assertIn("import numpy as np", content, 
                         "You need to import numpy with the alias 'np'")
        
        print("\nAll required libraries are correctly imported!")

if __name__ == '__main__':
    print("="*50)
    print("TESTING REQUIRED LIBRARIES")
    print("="*50)
    unittest.main(verbosity=2)
