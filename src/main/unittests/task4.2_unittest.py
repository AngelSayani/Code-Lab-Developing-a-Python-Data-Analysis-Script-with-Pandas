# Unit Test for Task 4.2: Plot Monthly Sales Function
import unittest
import os
import sys
import inspect
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for testing

# Add the parent directory to path so we can import the module
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..', 'python')
sys.path.append(parent_dir)

class TestPlotMonthlySalesFunction(unittest.TestCase):
    def setUp(self):
        # Create test data
        self.monthly_sales = pd.Series({'January': 250, 'March': 300, 'July': 250, 'December': 500})
        
        # Clean up any existing visualization file
        if os.path.exists('monthly_sales.png'):
            try:
                os.remove('monthly_sales.png')
            except (PermissionError, FileNotFoundError):
                pass
    
    def tearDown(self):
        # Clean up created file
        if os.path.exists('monthly_sales.png'):
            try:
                os.remove('monthly_sales.png')
            except (PermissionError, FileNotFoundError):
                pass
    
    def test_plot_monthly_sales_function(self):
        """Test that the plot_monthly_sales function exists and works correctly"""
        print(f"\nCHECKING TASK 4.2: PLOT MONTHLY SALES FUNCTION")
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
            if hasattr(sales_analysis, 'plot_monthly_sales'):
                plot_monthly_sales = getattr(sales_analysis, 'plot_monthly_sales')
                print("✓ Successfully imported plot_monthly_sales function")
            else:
                print("✗ ERROR: plot_monthly_sales function not found in sales_analysis module!")
                print("  SOLUTION: Create a function called 'plot_monthly_sales' in sales_analysis.py")
                self.fail("plot_monthly_sales function not found in sales_analysis module")
        except ImportError as e:
            print(f"✗ ERROR: Could not import sales_analysis module! {e}")
            print("  SOLUTION: Make sure sales_analysis.py exists and is valid Python code")
            self.fail(f"Could not import sales_analysis module: {e}")
        
        # Check if it's a function
        print("\nChecking if plot_monthly_sales is a function...")
        self.assertTrue(callable(plot_monthly_sales), 
                       "plot_monthly_sales is not a function")
        print("✓ plot_monthly_sales is correctly defined as a function")
        
        # Check function signature
        print("\nChecking function parameters...")
        sig = inspect.signature(plot_monthly_sales)
        params = list(sig.parameters.keys())
        self.assertTrue(len(params) == 1, 
                      f"plot_monthly_sales should take exactly 1 parameter, got {len(params)}")
        self.assertEqual(params[0], 'monthly', 
                        f"Parameter should be named 'monthly', got '{params[0]}'")
        print("✓ plot_monthly_sales takes the correct 'monthly' parameter")
        
        # Test the function with our test data
        print("\nTesting plot_monthly_sales with sample data...")
        try:
            plot_monthly_sales(self.monthly_sales)
            print("✓ Function executed without errors")
        except Exception as e:
            print(f"✗ ERROR: Function raised an exception: {e}")
            print("  SOLUTION: Fix the implementation of plot_monthly_sales")
            self.fail(f"plot_monthly_sales function raised an exception: {e}")
        
        # Check if file was created
        print("\nChecking if monthly_sales.png was created...")
        self.assertTrue(os.path.exists('monthly_sales.png'), 
                       "plot_monthly_sales should create a file called 'monthly_sales.png'")
        print("✓ monthly_sales.png was successfully created")
        
        # Check file size to ensure it's a valid image
        file_size = os.path.getsize('monthly_sales.png')
        print(f"File size: {file_size} bytes")
        self.assertGreater(file_size, 1000, 
                          "The generated image file is too small, it might not be a valid plot")
        print("✓ Image file has a reasonable size")
        
        print("\nTASK 4.2 COMPLETE! The plot_monthly_sales function works correctly.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
