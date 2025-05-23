# Unit Test for Data Loading Function (part of test_sales_analysis.py)
import unittest
import pandas as pd
from io import StringIO
from sales_analysis import load_data, clean_data

class TestDataLoading(unittest.TestCase):
    def setUp(self):
        # Create sample CSV data
        self.csv_data = """Date,Product,Category,Sales,Quantity
2023-01-15,Laptop,Electronics,1200.50,1
2023-02-20,Smartphone,Electronics,800.75,2
2023-03-10,T-shirt,Clothing,25.99,5
2023-04-05,Headphones,Electronics,150.25,3
2023-05-12,Jeans,Clothing,45.50,2
"""
        # Write sample data to a temporary file
        with open('test_sales.csv', 'w') as f:
            f.write(self.csv_data)
            
    def test_load_data(self):
        # Test that the function correctly loads CSV data
        df = load_data('test_sales.csv')
        
        # Check that the DataFrame has the expected shape
        self.assertEqual(df.shape, (5, 5))
        
        # Check that the DataFrame contains the expected columns
        expected_columns = ['Date', 'Product', 'Category', 'Sales', 'Quantity']
        self.assertListEqual(list(df.columns), expected_columns)
        
        # Check that the Sales column contains numeric data
        self.assertTrue(pd.api.types.is_numeric_dtype(df['Sales']))
        
    def test_clean_data(self):
        # Create a DataFrame with missing values
        data_with_na = """Date,Product,Category,Sales,Quantity
2023-01-15,Laptop,Electronics,1200.50,1
2023-02-20,,Electronics,800.75,2
2023-03-10,T-shirt,Clothing,,5
2023-04-05,Headphones,Electronics,150.25,3
"""
        df_with_na = pd.read_csv(StringIO(data_with_na))
        
        # Clean the data
        cleaned_df = clean_data(df_with_na)
        
        # Check that rows with missing values were removed
        self.assertEqual(cleaned_df.shape[0], 2)
        
        # Check that Date was converted to datetime
        self.assertTrue(pd.api.types.is_datetime64_dtype(cleaned_df['Date']))
        
        # Check that Month column was created
        self.assertIn('Month', cleaned_df.columns)

if __name__ == '__main__':
    unittest.main()
