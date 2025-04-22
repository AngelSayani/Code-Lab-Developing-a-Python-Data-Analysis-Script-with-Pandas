# Unit Test for Task 3.1: Create Sales by Category Function
import unittest
import os
import sys
import inspect
import pandas as pd

# Add the parent directory to path so we can import the module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..', 'python')
sys.path.append(parent_dir)

class TestSalesByCategoryFunction(unittest.TestCase):
    def setUp(self):
        # Create test data
        self.test_data = pd.DataFrame({
            'Category': ['Electronics', 'Clothing', 'Electronics', 'Home', 'Clothing'],
            'Sales': [1000, 500, 1500, 800, 600]
        })
    
    def test_sales_by_category_function(self):
        """Test that the sales_by_category function exists and works correctly"""
        print(f"\nCHECKING TASK 3.1: CREATE SALES BY CATEGORY FUNCTION")
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
            if hasattr(sales_analysis, 'sales_by_category'):
                sales_by_category = getattr(sales_analysis, 'sales_by_category')
                print("✓ Successfully imported sales_by_category function")
            else:
                print("✗ ERROR: sales_by_category function not found in sales_analysis module!")
                print("  SOLUTION: Create a function called 'sales_by_category' in sales_analysis.py")
                self.fail("sales_by_category function not found in sales_analysis module")
        except ImportError as e:
            print(f"✗ ERROR: Could not import sales_analysis module! {e}")
            print("  SOLUTION: Make sure sales_analysis.py exists and is valid Python code")
            self.fail(f"Could not import sales_analysis module: {e}")
        
        # Check if it's a function
        print("\nChecking if sales_by_category is a function...")
        self.assertTrue(callable(sales_by_category), 
                       "sales_by_category is not a function")
        print("✓ sales_by_category is correctly defined as a function")
        
        # Check function signature
        print("\nChecking function parameters...")
        sig = inspect.signature(sales_by_category)
        params = list(sig.parameters.keys())
        self.assertTrue(len(params) == 1, 
                      f"sales_by_category should take exactly 1 parameter, got {len(params)}")
        self.assertEqual(params[0], 'df', 
                        f"Parameter should be named 'df', got '{params[0]}'")
        print("✓ sales_by_category takes the correct 'df' parameter")
        
        # Test the function with our test data
        print("\nTesting sales_by_category with sample data...")
        try:
            result = sales_by_category(self.test_data)
            print("✓ Function executed without errors")
        except Exception as e:
            print(f"✗ ERROR: Function raised an exception: {e}")
            print("  SOLUTION: Fix the implementation of sales_by_category")
            self.fail(f"sales_by_category function raised an exception: {e}")
        
        # Check return type
        print("\nChecking return value...")
        self.assertIsInstance(result, pd.Series, 
                             "sales_by_category should return a pandas Series")
        print("✓ Function correctly returns a pandas Series")
        
        # Check groupby operation
        print("\nChecking aggregation by category...")
        expected_values = {'Electronics': 2500, 'Clothing': 1100, 'Home': 800}
        
        all_categories_present = True
        for category, expected_sales in expected_values.items():
            if category in result:
                if result[category] == expected_sales:
                    print(f"✓ {category} correctly aggregated to ${expected_sales}")
                else:
                    print(f"✗ ERROR: {category} has sales of ${result[category]}, expected ${expected_sales}")
                    all_categories_present = False
            else:
                print(f"✗ ERROR: {category} is missing from the results")
                all_categories_present = False
        
        self.assertTrue(all_categories_present, "Categories not correctly aggregated")
        
        # Check sorting order
        print("\nChecking sorting order...")
        categories_in_order = list(result.index)
        expected_order = ['Electronics', 'Clothing', 'Home']
        
        if categories_in_order == expected_order:
            print("✓ Categories are correctly sorted by sales in descending order")
        else:
            print(f"✗ ERROR: Categories are not sorted correctly. Expected: {expected_order}, Got: {categories_in_order}")
            print("  SOLUTION: Add .sort_values(ascending=False) after the groupby operation")
            self.assertEqual(categories_in_order, expected_order, 
                           "Categories should be sorted by sales in descending order")
        
        print("\nTASK 3.1 COMPLETE! The sales_by_category function works correctly.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
