# Unit Test for Task 5.2: Sales Statistics Function
import unittest
import os
import sys
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
        print("✓ sales_statistics is correctly defined as a function")
        
        # Test the function with our test data
        print("\nTesting sales_statistics with sample data...")
        try:
            stats = sales_statistics(self.test_data)
            print("✓ Function executed without errors")
        except Exception as e:
            print(f"✗ ERROR: Function raised an exception: {e}")
            print("  SOLUTION: Fix the implementation of sales_statistics")
            self.fail(f"sales_statistics function raised an exception: {e}")
        
        # Check return type
        print("\nChecking return value...")
        self.assertIsInstance(stats, dict, 
                             "sales_statistics should return a dictionary")
        print("✓ Function correctly returns a dictionary")
        
        # Check required statistics
        print("\nChecking statistics calculations...")
        required_stats = ['total_sales', 'average_sale', 'max_sale', 'min_sale', 'sale_std_dev']
        
        all_stats_present = True
        for stat in required_stats:
            if stat in stats:
                print(f"✓ '{stat}' is included in the statistics")
            else:
                print(f"✗ ERROR: '{stat}' is missing from the statistics")
                all_stats_present = False
        
        self.assertTrue(all_stats_present, "Not all required statistics are included")
        
        # Check specific values
        print("\nVerifying statistics calculations...")
        expected_values = {
            'total_sales': np.sum(self.test_data['Sales']),
            'average_sale': np.mean(self.test_data['Sales']),
            'max_sale': np.max(self.test_data['Sales']),
            'min_sale': np.min(self.test_data['Sales']),
            'sale_std_dev': np.std(self.test_data['Sales'], ddof=1)
        }
        
        for stat, expected in expected_values.items():
            actual = stats[stat]
            # Allow for floating point precision issues
            if abs(actual - expected) < 0.01:
                print(f"✓ '{stat}' is correctly calculated as {actual:.2f}")
            else:
                print(f"✗ ERROR: '{stat}' is {actual:.2f}, expected {expected:.2f}")
                print(f"  SOLUTION: Check the calculation for {stat}")
                self.assertAlmostEqual(actual, expected, delta=0.01, 
                                    msg=f"Expected {stat} to be {expected}, got {actual}")
        
        print("\nTASK 5.2 COMPLETE! The sales_statistics function works correctly.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
