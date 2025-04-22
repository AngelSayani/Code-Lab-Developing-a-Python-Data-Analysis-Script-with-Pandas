# Unit Test for Task 5.1: Top Products Function
import unittest
import os
import sys
import inspect
import pandas as pd

# Add the parent directory to path so we can import the module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..', 'python')
sys.path.append(parent_dir)

class TestTopProductsFunction(unittest.TestCase):
    def setUp(self):
        # Create test data
        self.test_data = pd.DataFrame({
            'Product': ['Laptop', 'Smartphone', 'Headphones', 'Laptop', 'Smartphone', 'TV'],
            'Sales': [1200, 800, 150, 1300, 750, 1500]
        })
    
    def test_top_products_function(self):
        """Test that the top_products function exists and works correctly"""
        print(f"\nCHECKING TASK 5.1: TOP PRODUCTS FUNCTION")
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
            if hasattr(sales_analysis, 'top_products'):
                top_products = getattr(sales_analysis, 'top_products')
                print("✓ Successfully imported top_products function")
            else:
                print("✗ ERROR: top_products function not found in sales_analysis module!")
                print("  SOLUTION: Create a function called 'top_products' in sales_analysis.py")
                self.fail("top_products function not found in sales_analysis module")
        except ImportError as e:
            print(f"✗ ERROR: Could not import sales_analysis module! {e}")
            print("  SOLUTION: Make sure sales_analysis.py exists and is valid Python code")
            self.fail(f"Could not import sales_analysis module: {e}")
        
        # Check if it's a function
        print("\nChecking if top_products is a function...")
        self.assertTrue(callable(top_products), 
                       "top_products is not a function")
        print("✓ top_products is correctly defined as a function")
        
        # Check function signature
        print("\nChecking function parameters...")
        sig = inspect.signature(top_products)
        params = list(sig.parameters.keys())
        self.assertTrue(len(params) == 1, 
                      f"top_products should take exactly 1 parameter, got {len(params)}")
        self.assertEqual(params[0], 'df', 
                        f"Parameter should be named 'df', got '{params[0]}'")
        print("✓ top_products takes the correct 'df' parameter")
        
        # Test the function with our test data
        print("\nTesting top_products with sample data...")
        try:
            result = top_products(self.test_data)
            print("✓ Function executed without errors")
        except Exception as e:
            print(f"✗ ERROR: Function raised an exception: {e}")
            print("  SOLUTION: Fix the implementation of top_products")
            self.fail(f"top_products function raised an exception: {e}")
        
        # Check return type
        print("\nChecking return value...")
        self.assertIsInstance(result, pd.DataFrame, 
                             "top_products should return a pandas DataFrame")
        print("✓ Function correctly returns a pandas DataFrame")
        
        # Check DataFrame structure
        print("\nChecking DataFrame structure...")
        self.assertEqual(list(result.columns), ['Product', 'Sales'], 
                        f"Expected columns ['Product', 'Sales'], got {list(result.columns)}")
        print("✓ DataFrame has the correct columns")
        
        # Check number of products
        print("\nChecking top products count...")
        self.assertLessEqual(len(result), 5, 
                            f"Expected at most 5 products, got {len(result)}")
        print(f"✓ Function returns the correct number of products: {len(result)}")
        
        # Check the top product
        print("\nChecking top product ranking...")
        expected_top_product = 'TV'
        if len(result) > 0 and result.iloc[0]['Product'] == expected_top_product:
            print(f"✓ Top product is correctly identified as '{expected_top_product}'")
        else:
            if len(result) == 0:
                print("✗ ERROR: Result DataFrame is empty!")
            else:
                print(f"✗ ERROR: Expected top product to be '{expected_top_product}', got '{result.iloc[0]['Product']}'")
            print("  SOLUTION: Make sure your function sorts products by Sales in descending order")
            self.assertTrue(len(result) > 0 and result.iloc[0]['Product'] == expected_top_product, 
                          f"Expected top product to be '{expected_top_product}'")
        
        print("\nTASK 5.1 COMPLETE! The top_products function works correctly.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
