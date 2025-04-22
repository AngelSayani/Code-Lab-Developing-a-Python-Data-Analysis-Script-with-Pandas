# Unit Test for Task 4.1: Plot Sales by Category Function
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

class TestPlotCategorySalesFunction(unittest.TestCase):
    def setUp(self):
        # Create test data
        self.category_sales = pd.Series({'Electronics': 2500, 'Clothing': 1100, 'Home': 800})
        
        # Clean up any existing visualization file
        if os.path.exists('category_sales.png'):
            try:
                os.remove('category_sales.png')
            except (PermissionError, FileNotFoundError):
                pass
    
    def tearDown(self):
        # Clean up created file
        if os.path.exists('category_sales.png'):
            try:
                os.remove('category_sales.png')
            except (PermissionError, FileNotFoundError):
                pass
    
    def test_plot_category_sales_function(self):
        """Test that the plot_category_sales function exists and works correctly"""
        print(f"\nCHECKING TASK 4.1: PLOT SALES BY CATEGORY FUNCTION")
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
            if hasattr(sales_analysis, 'plot_category_sales'):
                plot_category_sales = getattr(sales_analysis, 'plot_category_sales')
                print("✓ Successfully imported plot_category_sales function")
            else:
                print("✗ ERROR: plot_category_sales function not found in sales_analysis module!")
                print("  SOLUTION: Create a function called 'plot_category_sales' in sales_analysis.py")
                self.fail("plot_category_sales function not found in sales_analysis module")
        except ImportError as e:
            print(f"✗ ERROR: Could not import sales_analysis module! {e}")
            print("  SOLUTION: Make sure sales_analysis.py exists and is valid Python code")
            self.fail(f"Could not import sales_analysis module: {e}")
        
        # Check if it's a function
        print("\nChecking if plot_category_sales is a function...")
        self.assertTrue(callable(plot_category_sales), 
                       "plot_category_sales is not a function")
        print("✓ plot_category_sales is correctly defined as a function")
        
        # Check function signature
        print("\nChecking function parameters...")
        sig = inspect.signature(plot_category_sales)
        params = list(sig.parameters.keys())
        self.assertTrue(len(params) == 1, 
                      f"plot_category_sales should take exactly 1 parameter, got {len(params)}")
        self.assertEqual(params[0], 'category_sales', 
                        f"Parameter should be named 'category_sales', got '{params[0]}'")
        print("✓ plot_category_sales takes the correct 'category_sales' parameter")
        
        # Test the function with our test data
        print("\nTesting plot_category_sales with sample data...")
        try:
            plot_category_sales(self.category_sales)
            print("✓ Function executed without errors")
        except Exception as e:
            print(f"✗ ERROR: Function raised an exception: {e}")
            print("  SOLUTION: Fix the implementation of plot_category_sales")
            self.fail(f"plot_category_sales function raised an exception: {e}")
        
        # Check if file was created
        print("\nChecking if category_sales.png was created...")
        self.assertTrue(os.path.exists('category_sales.png'), 
                       "plot_category_sales should create a file called 'category_sales.png'")
        print("✓ category_sales.png was successfully created")
        
        # Check file size to ensure it's a valid image
        file_size = os.path.getsize('category_sales.png')
        print(f"File size: {file_size} bytes")
        self.assertGreater(file_size, 1000, 
                          "The generated image file is too small, it might not be a valid plot")
        print("✓ Image file has a reasonable size")
        
        print("\nTASK 4.1 COMPLETE! The plot_category_sales function works correctly.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
