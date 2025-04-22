# Unit Test for Task 2.1: Create Clean Data Function
import unittest
import os
import sys
import inspect
import pandas as pd
from io import StringIO

# Add the parent directory to path so we can import the module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..', 'python')
sys.path.append(parent_dir)

class TestCleanDataFunction(unittest.TestCase):
    def setUp(self):
        # Create test data with missing values
        data = """Date,Product,Category,Sales,Quantity
2023-01-15,Laptop,Electronics,1200.50,1
2023-02-20,,Electronics,800.75,2
2023-03-10,T-shirt,Clothing,,5
2023-04-05,Headphones,Electronics,150.25,3
"""
        self.df_with_na = pd.read_csv(StringIO(data))
    
    def test_clean_data_function(self):
        """Test that the clean_data function exists and works correctly"""
        print(f"\nCHECKING TASK 2.1: CREATE CLEAN DATA FUNCTION")
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
            if hasattr(sales_analysis, 'clean_data'):
                clean_data = getattr(sales_analysis, 'clean_data')
                print("✓ Successfully imported clean_data function")
            else:
                print("✗ ERROR: clean_data function not found in sales_analysis module!")
                print("  SOLUTION: Create a function called 'clean_data' in sales_analysis.py")
                self.fail("clean_data function not found in sales_analysis module")
        except ImportError as e:
            print(f"✗ ERROR: Could not import sales_analysis module! {e}")
            print("  SOLUTION: Make sure sales_analysis.py exists and is valid Python code")
            self.fail(f"Could not import sales_analysis module: {e}")
        
        # Check if it's a function
        print("\nChecking if clean_data is a function...")
        self.assertTrue(callable(clean_data), 
                       "clean_data is not a function")
        print("✓ clean_data is correctly defined as a function")
        
        # Check function signature
        print("\nChecking function parameters...")
        sig = inspect.signature(clean_data)
        params = list(sig.parameters.keys())
        self.assertTrue(len(params) == 1, 
                      f"clean_data should take exactly 1 parameter, got {len(params)}")
        self.assertEqual(params[0], 'df', 
                        f"Parameter should be named 'df', got '{params[0]}'")
        print("✓ clean_data takes the correct 'df' parameter")
        
        # Test the function with our test data
        print("\nTesting clean_data with sample data containing missing values...")
        try:
            cleaned_df = clean_data(self.df_with_na)
            print("✓ Function executed without errors")
        except Exception as e:
            print(f"✗ ERROR: Function raised an exception: {e}")
            print("  SOLUTION: Fix the implementation of clean_data to handle missing values correctly")
            self.fail(f"clean_data function raised an exception: {e}")
        
        # Check return type
        print("\nChecking return value...")
        self.assertIsInstance(cleaned_df, pd.DataFrame, 
                             "clean_data should return a pandas DataFrame")
        print("✓ Function correctly returns a pandas DataFrame")
        
        # Check if rows with missing values were removed
        print("\nChecking handling of missing values...")
        if cleaned_df.shape[0] < self.df_with_na.shape[0]:
            print(f"✓ Rows with missing values were removed ({self.df_with_na.shape[0]} -> {cleaned_df.shape[0]})")
        else:
            print("✗ ERROR: Rows with missing values were not removed!")
            print("  SOLUTION: Use df.dropna() to remove rows with missing values")
            self.assertLess(cleaned_df.shape[0], self.df_with_na.shape[0], 
                          "clean_data should remove rows with missing values")
        
        # Check if Date was converted to datetime
        print("\nChecking date conversion...")
        if pd.api.types.is_datetime64_dtype(cleaned_df['Date']):
            print("✓ Date column was correctly converted to datetime")
        else:
            print("✗ ERROR: Date column was not converted to datetime!")
            print("  SOLUTION: Use pd.to_datetime(df['Date']) to convert Date column")
            self.assertTrue(pd.api.types.is_datetime64_dtype(cleaned_df['Date']), 
                          "Date column should be converted to datetime format")
        
        # Check if Month column was created
        print("\nChecking Month column creation...")
        if 'Month' in cleaned_df.columns:
            print("✓ Month column was correctly created")
            
            # Check if Month column contains month names
            if cleaned_df['Month'].iloc[0] in ['January', 'February', 'March', 'April', 'May', 'June', 
                                             'July', 'August', 'September', 'October', 'November', 'December']:
                print("✓ Month column contains correct month names")
            else:
                print(f"✗ ERROR: Month column does not contain proper month names! Got '{cleaned_df['Month'].iloc[0]}'")
                print("  SOLUTION: Use df['Date'].dt.month_name() to get month names")
                self.assertIn(cleaned_df['Month'].iloc[0], 
                            ['January', 'February', 'March', 'April', 'May', 'June', 
                             'July', 'August', 'September', 'October', 'November', 'December'],
                            "Month column should contain proper month names")
        else:
            print("✗ ERROR: Month column was not created!")
            print("  SOLUTION: Add df['Month'] = df['Date'].dt.month_name()")
            self.assertIn('Month', cleaned_df.columns, 
                         "clean_data should create a new 'Month' column")
        
        print("\nTASK 2.1 COMPLETE! The clean_data function works correctly.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
