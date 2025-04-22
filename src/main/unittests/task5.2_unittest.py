# Unit Test for Task 5.2: Sales Statistics Function
import unittest
import os
import sys
import inspect
import pandas as pd
import numpy as np

# Add the parent directory to path so we can import the module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..', 'python')
sys.path.append(parent_dir)

class TestSalesStatisticsFunction(unittest.TestCase):
    def setUp(self):
        # Create test data
        self.test_data = pd.DataFrame({
            'Sales': [1200, 800, 150, 1300, 750, 1500]
        })
    
    def test_sales_statistics_function(self):
        """Test that the sales_statistics function exists and works correctly"""
        print(f"\nCHECKING TASK 5.2: SALES STATISTICS FUNCTION")
        print("="*50)
        
        # Check if the file exists
        file_path = os.path.join(parent_dir, 'sales_analysis.py')
        print(f"Checking if {file_path} exists...")
        self.assertTrue(os.path.exists(file_path), 
                        f"sales_analysis.py file not found. Make sure it's in the correct location.")
        print(f"File found at {file_path}")
        
        # Import the module
        print("\nImporting the sales_analysis module...")
        try:
            # This import should now work with the updated path
            import sales_analysis
            if hasattr(sales_analysis, 'sales_statistics'):
                sales_statistics = getattr(sales_analysis, 'sales_statistics')
                print("✓ Successfully imported sales_statistics function")
            else:
                print("✗ ERROR: sales_statistics function not found in sales_analysis module!")
                print("  SOLUTION: Create a function called 'sales_statistics' in sales_analysis.py")
                self.fail("sales_statistics function not found in sales_analysis module")
        except ImportError as e:
            print(f"✗ ERROR: Could not import sales_analysis module! {e}")
            print("  SOLUTION: Make sure sales_analysis.py exists and is valid Python code")
            self.fail(f"Could not import sales_analysis module: {e}")
        
        # Check if it's a function
        print("\nChecking if sales_statistics is a function...")
        self.assertTrue(callable(sales_statistics), 
                       "sales_statistics is not a function")
        print
