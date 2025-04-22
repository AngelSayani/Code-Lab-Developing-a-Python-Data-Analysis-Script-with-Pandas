# Unit Test for Task 2: Load Sales Data Function
import unittest
import os
import sys
import inspect
import pandas as pd
import tempfile

class TestLoadDataFunction(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
        with open(self.temp_file.name, 'w') as f:
            f.write("Date,Product,Category,Sales,Quantity\n")
            f.write("2023-01-15,Laptop,Electronics,1200.50,1\n")
    
    def tearDown(self):
        # Remove temporary file
        os.unlink(self.temp_file.name)
    
    def test_load_data_function(self):
        """Test that the load_data function exists and works correctly"""
        print(f"\nCHECKING TASK 2: LOAD SALES DATA FUNCTION")
        print("="*50)
        
        # Check if the file exists
        file_path = os.path.join('src', 'main', 'python', 'sales_analysis.py')
        print(f"Checking if {file_path} exists...")
        self.assertTrue(os.path.exists(file_path), 
                        f"sales_analysis.py file not found. Make sure it's in the correct location.")
        print(f"File found at {file_path}")
        
        # Import the module
        print("\nImporting the sales_analysis module...")
        sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(file_path)))))
        try:
            from src.main.python.sales_analysis import load_data
            print("✓ Successfully imported load_data function")
        except ImportError:
            print("✗ ERROR: Could not import load_data function!")
            print("  SOLUTION: Create a function called 'load_data' in sales_analysis.py")
            self.fail("Could not import load_data function from sales_analysis.py")
        
        # Check if it's a function
        print("\nChecking if load_data is a function...")
        self.assertTrue(callable(load_data), 
                       "load_data is not a function")
        print("✓ load_data is correctly defined as a function")
        
        # Check function signature
        print("\nChecking function parameters...")
        sig = inspect.signature(load_data)
        params = list(sig.parameters.keys())
        self.assertIn('filename', params, 
                     "load_data function should take a parameter called 'filename'")
        print("✓ load_data takes the correct 'filename' parameter")
        
        # Test the function with our temp file
        print("\nTesting load_data with sample CSV file...")
        try:
            result = load_data(self.temp_file.name)
            print("✓ Function executed without errors")
        except Exception as e:
            print(f"✗ ERROR: Function raised an exception: {e}")
            print("  SOLUTION: Fix the implementation of load_data to handle CSV files correctly")
            self.fail(f"load_data function raised an exception: {e}")
        
        # Check return type
        print("\nChecking return value...")
        self.assertIsInstance(result, pd.DataFrame, 
                             "load_data should return a pandas DataFrame")
        print("✓ Function correctly returns a pandas DataFrame")
        
        # Check DataFrame structure
        print("\nChecking DataFrame structure...")
        self.assertEqual(result.shape, (1, 5), 
                        f"Expected DataFrame with 1 row and 5 columns, got {result.shape}")
        print(f"✓ DataFrame has the correct shape: {result.shape}")
        
        expected_columns = ['Date', 'Product', 'Category', 'Sales', 'Quantity']
        self.assertListEqual(list(result.columns), expected_columns, 
                            f"Expected columns {expected_columns} but got {list(result.columns)}")
        print("✓ DataFrame has the correct column names")
        
        # Check numeric columns
        print("\nChecking data types...")
        self.assertTrue(pd.api.types.is_numeric_dtype(result['Sales']), 
                       "Sales column should be numeric")
        print("✓ 'Sales' column is correctly parsed as numeric")
        
        print("\nTASK 2 COMPLETE! The load_data function works correctly.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
