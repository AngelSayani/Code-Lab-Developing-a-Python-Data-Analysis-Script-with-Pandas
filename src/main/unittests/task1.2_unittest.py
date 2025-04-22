# Unit Test for Task 1.2: Load Sales Data from CSV
import unittest
import os
import sys
import inspect
import pandas as pd
import tempfile

# Add the parent directory to path so we can import the module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..', 'python')
sys.path.append(parent_dir)

class TestLoadDataFunction(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
        self.temp_filename = self.temp_file.name
        with open(self.temp_filename, 'w') as f:
            f.write("Date,Product,Category,Sales,Quantity\n")
            f.write("2023-01-15,Laptop,Electronics,1200.50,1\n")
        self.temp_file.close()  # Close the file to avoid the lock issue
    
    def tearDown(self):
        # Remove temporary file
        try:
            os.unlink(self.temp_filename)
        except (PermissionError, FileNotFoundError):
            pass  # Ignore errors if file can't be deleted
    
    def test_load_data_function(self):
        """Test that the load_data function exists and works correctly"""
        print(f"\nCHECKING TASK 1.2: LOAD SALES DATA FROM CSV")
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
            if hasattr(sales_analysis, 'load_data'):
                load_data = getattr(sales_analysis, 'load_data')
                print("✓ Successfully imported load_data function")
            else:
                print("✗ ERROR: load_data function not found in sales_analysis module!")
                print("  SOLUTION: Create a function called 'load_data' in sales_analysis.py")
                self.fail("load_data function not found in sales_analysis module")
        except ImportError as e:
            print(f"✗ ERROR: Could not import sales_analysis module! {e}")
            print("  SOLUTION: Make sure sales_analysis.py exists and is valid Python code")
            self.fail(f"Could not import sales_analysis module: {e}")
        
        # The rest of your test remains the same...
        # Check if it's a function
        print("\nChecking if load_data is a function...")
        self.assertTrue(callable(load_data), 
                       "load_data is not a function")
        print("✓ load_data is correctly defined as a function")
        
        # Test the function with our temp file
        print("\nTesting load_data with sample CSV file...")
        try:
            result = load_data(self.temp_filename)
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
        
        # Check content parsing
        print("\nChecking data parsing...")
        self.assertEqual(result.iloc[0]['Product'], 'Laptop', 
                        f"Expected 'Laptop' in Product column, got '{result.iloc[0]['Product']}'")
        print("✓ DataFrame content is correctly parsed")
        
        # Check numeric columns
        print("\nChecking data types...")
        self.assertTrue(pd.api.types.is_numeric_dtype(result['Sales']), 
                       "Sales column should be numeric")
        print("✓ 'Sales' column is correctly parsed as numeric")
        
        print("\nTASK 1.2 COMPLETE! The load_data function works correctly.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
