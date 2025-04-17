import unittest
import pandas as pd
from io import StringIO
import os
import tempfile
import sys

# Try to import the functions
try:
    from sales_analysis import load_data, clean_data
    print("Successfully imported functions from sales_analysis")
except ImportError as e:
    print(f"ERROR importing from sales_analysis: {e}")
    sys.exit(1)

class TestDataAnalysis(unittest.TestCase):
    def setUp(self):
        print("Setting up test...")
        # Create sample CSV data
        self.csv_data = """Date,Product,Category,Sales,Quantity
2023-01-15,Laptop,Electronics,1200.50,1
2023-02-20,Smartphone,Electronics,800.75,2
2023-03-10,T-shirt,Clothing,25.99,5
2023-04-05,Headphones,Electronics,150.25,3
2023-05-12,Jeans,Clothing,45.50,2
"""
        # Create a temporary file
        try:
            self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
            with open(self.temp_file.name, 'w') as f:
                f.write(self.csv_data)
            print(f"Created temporary test file at: {self.temp_file.name}")
        except Exception as e:
            print(f"ERROR creating temp file: {e}")
            raise
            
    def tearDown(self):
        # Remove the temporary file
        try:
            os.unlink(self.temp_file.name)
            print(f"Removed temporary test file: {self.temp_file.name}")
        except Exception as e:
            print(f"ERROR removing temp file: {e}")
            
    def test_load_data(self):
        print("\nTesting load_data function...")
        # Test the load_data function
        df = load_data(self.temp_file.name)
        
        # Check that the DataFrame has the expected shape
        self.assertEqual(df.shape, (5, 5), f"Expected shape (5, 5) but got {df.shape}")
        
        # Check that the DataFrame contains the expected columns
        expected_columns = ['Date', 'Product', 'Category', 'Sales', 'Quantity']
        self.assertListEqual(list(df.columns), expected_columns, 
                            f"Expected columns {expected_columns} but got {list(df.columns)}")
        
        # Check that the Sales column contains numeric data
        self.assertTrue(pd.api.types.is_numeric_dtype(df['Sales']), 
                       "Sales column should be numeric")
        print("load_data test passed!")
        
    def test_clean_data(self):
        print("\nTesting clean_data function...")
        # Create a DataFrame with missing values
        data_with_na = """Date,Product,Category,Sales,Quantity
2023-01-15,Laptop,Electronics,1200.50,1
2023-02-20,,Electronics,800.75,2
2023-03-10,T-shirt,Clothing,,5
2023-04-05,Headphones,Electronics,150.25,3
"""
        print("Created test data with missing values")
        df_with_na = pd.read_csv(StringIO(data_with_na))
        
        # Clean the data
        cleaned_df = clean_data(df_with_na)
        
        # Check that rows with missing values were removed
        self.assertLess(cleaned_df.shape[0], df_with_na.shape[0], 
                       f"Expected fewer rows after cleaning but got {cleaned_df.shape[0]} (was {df_with_na.shape[0]})")
        
        # Check that Date was converted to datetime
        self.assertTrue(pd.api.types.is_datetime64_dtype(cleaned_df['Date']), 
                       "Date column should be datetime type")
        
        # Check that Month column was created
        self.assertIn('Month', cleaned_df.columns, 
                     f"Month column missing from {cleaned_df.columns}")
        print("clean_data test passed!")

if __name__ == '__main__':
    print("="*50)
    print("RUNNING SALES ANALYSIS TESTS")
    print("="*50)
    try:
        unittest.main()
    except Exception as e:
        print(f"ERROR running tests: {e}")
        import traceback
        traceback.print_exc()
