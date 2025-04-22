# Unit Test for Task 3.2: Create Monthly Sales Function
import unittest
import os
import sys
import inspect
import pandas as pd
import re

# Add the parent directory to path so we can import the module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..', 'python')
sys.path.append(parent_dir)

class TestMonthlySalesFunction(unittest.TestCase):
    def setUp(self):
        # Create test data
        self.test_data = pd.DataFrame({
            'Month': ['January', 'March', 'December', 'January', 'July'],
            'Sales': [100, 300, 500, 150, 250]
        })
    
    def test_monthly_sales_function(self):
        """Test that the monthly_sales function exists and works correctly"""
        print(f"\nCHECKING TASK 3.2: CREATE MONTHLY SALES FUNCTION")
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
            if hasattr(sales_analysis, 'monthly_sales'):
                monthly_sales = getattr(sales_analysis, 'monthly_sales')
                print("✓ Successfully imported monthly_sales function")
            else:
                print("✗ ERROR: monthly_sales function not found in sales_analysis module!")
                print("  SOLUTION: Create a function called 'monthly_sales' in sales_analysis.py")
                self.fail("monthly_sales function not found in sales_analysis module")
        except ImportError as e:
            print(f"✗ ERROR: Could not import sales_analysis module! {e}")
            print("  SOLUTION: Make sure sales_analysis.py exists and is valid Python code")
            self.fail(f"Could not import sales_analysis module: {e}")
        
        # Check if it's a function
        print("\nChecking if monthly_sales is a function...")
        self.assertTrue(callable(monthly_sales), 
                       "monthly_sales is not a function")
        print("✓ monthly_sales is correctly defined as a function")
        
        # Check function signature
        print("\nChecking function parameters...")
        sig = inspect.signature(monthly_sales)
        params = list(sig.parameters.keys())
        self.assertTrue(len(params) == 1, 
                      f"monthly_sales should take exactly 1 parameter, got {len(params)}")
        self.assertEqual(params[0], 'df', 
                        f"Parameter should be named 'df', got '{params[0]}'")
        print("✓ monthly_sales takes the correct 'df' parameter")
        
        # Test the function with our test data
        print("\nTesting monthly_sales with sample data...")
        try:
            result = monthly_sales(self.test_data)
            print("✓ Function executed without errors")
        except Exception as e:
            print(f"✗ ERROR: Function raised an exception: {e}")
            print("  SOLUTION: Fix the implementation of monthly_sales")
            self.fail(f"monthly_sales function raised an exception: {e}")
        
        # Check return type
        print("\nChecking return value...")
        self.assertIsInstance(result, pd.Series, 
                             "monthly_sales should return a pandas Series")
        print("✓ Function correctly returns a pandas Series")
        
        # Check groupby operation
        print("\nChecking aggregation by month...")
        expected_values = {'January': 250, 'March': 300, 'July': 250, 'December': 500}
        
        all_months_present = True
        for month, expected_sales in expected_values.items():
            if month in result:
                if result[month] == expected_sales:
                    print(f"✓ {month} correctly aggregated to ${expected_sales}")
                else:
                    print(f"✗ ERROR: {month} has sales of ${result[month]}, expected ${expected_sales}")
                    all_months_present = False
            else:
                print(f"✗ ERROR: {month} is missing from the results")
                all_months_present = False
        
        self.assertTrue(all_months_present, "Months not correctly aggregated")
        
        # Check if months_order list is defined
        print("\nChecking for months_order list...")
        with open(file_path, 'r') as f:
            content = f.read()
        
        months_order_pattern = r"months_order\s*=\s*\[\s*['\"]January['\"]\s*,.*?['\"]December['\"]\s*\]"
        if re.search(months_order_pattern, content, re.DOTALL):
            print("✓ months_order list is defined with all 12 months")
        else:
            print("✗ ERROR: months_order list is missing or incomplete!")
            print("  SOLUTION: Add a complete months_order list with all 12 months")
            self.assertTrue(re.search(months_order_pattern, content, re.DOTALL), 
                          "months_order list should be defined with all 12 months")
        
        # Check for reindex operation
        print("\nChecking for reindex operation...")
        reindex_pattern = r"monthly\s*=\s*monthly\.reindex\s*\(\s*months_order\s*\)"
        if re.search(reindex_pattern, content):
            print("✓ reindex operation is used to order months chronologically")
        else:
            print("✗ ERROR: reindex operation is missing!")
            print("  SOLUTION: Add 'monthly = monthly.reindex(months_order)' to order months")
            self.assertTrue(re.search(reindex_pattern, content), 
                          "reindex should be used to order months chronologically")
        
        print("\nTASK 3.2 COMPLETE! The monthly_sales function works correctly.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
